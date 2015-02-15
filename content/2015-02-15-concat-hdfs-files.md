Title: Failing to concat HDFS files
Tags: hadoop, documentation
Date: 2015-02-15T00:32

At work I use [Hadoop][hadoop] via [Cascading][cascading]. I wanted the final output of a multi-stage job to be a single file. This is more complicated that I'd hoped, and led me down some blind alleys where Google wasn't helping. Hopefully this article will help others hitting the same issue.

### Using a single reducer
I was initially doing this with [job.setNumReduceTasks(0)][set-num-reduce-tasks], which restricted the job to use only a single reducer. The *side effect* is that it writes out to a single file, but depending on what's going on in that reduce, you don't want it running single threaded. Also, if Cascading's flow planner puts a map-side operation as that last thing that needs doing, then you might still get multiple output files.

### Using `getmerge`
My search for [hdfs merge single file][google-results] turned up [various][getmerge1] [answers][getmerge2] [recommending][getmerge3] the `hadoop -getmerge` command. This is great if you want to merge from hdfs files to a single **local** file. If you want everything staying on HDFS, this is a mistake since it streams everything locally, then pushes it back. This will get worse and worse as you get more data.

### Using FileSystem.concat(...)
*This way lies madness*

Browsing through Hadoop's [FileSystem][org.apache.hadoop.fs.FileSystem] class, I found [the following function][org.apache.hadoop.fs.FileSystem.concat]:

    FileSystem.concat(Path trg, Path[] psrcs)

    Concat existing files together.

    Parameters:
        trg - the path to the target destination.
        psrcs - the paths to the sources to use for the concatenation.

Fantastic! This is probably what I want. Turns out to be the opposite of what I want, and not at all what I expected from the documentation:

1. The source files will be removed. This is in a javadoc at [DFSClient.java:1566][sources-removed]. Good to know
2. All paths (source and destination) must be in the same directory (this is in an in-line comment at [FSNamesystem:1580][same-directory])
3. The destination must exist. Found that out when a call to getInode on [FSNamesystem:1633][must-exist] fails if the file does not exist. Fine, I'll create an empty file.
4. The destination file must not be empty. This is "by design" according to [FSNamesystem:1639][must-not-be-empty]. Fine, I'll create a new file with a blank line.
5. The destination file must have the last block full ([FSNamesystem:1654][must-have-last-block-full]). Why would that be a requirement.

This makes it unusable as a general purpose "concat these files together" since I can't concat to a non-existing file, I can't concat to a blank file, and I can't somehow align the blocks. Luckily this bug has been closed as "not a problem" in [HDFS-6641][HDFS-6641].

This all boils down to `FileSystem.concat(...)` not being for concatenating multiple files like most people would think of it. I think it's explained wrong. It's for **moving the blocks of many files into a single file**. It's a **namenode only** operation in that it remaps blocks without doing any copying. Once that's the purpose, everything else falls into place. The last block of `trg` must be full, since a file can't have a non-full block in the middle. The `psrcs` files disappear because this isn't a copy. The "same directory" and "trg not empty" restrictions still make no sense, but whatever.

This is not the api you are looking for. The documentation is misleading, but I filed [HDFS-7800][HDFS-7800] to hopefully improve that.

### Force a useless map-reduce cycle

The solution I went with was to use `job.setNumReduceTasks(0)`, but force a useless map-reduce at the end of my Cascading flow. This is inefficient, but atleast the reducer does nothing but write down data, so it's pretty fast.

[hadoop]: https://hadoop.apache.org/
[cascading]: http://www.cascading.org/
[set-num-reduce-tasks]: https://hadoop.apache.org/docs/current/api/org/apache/hadoop/mapred/JobConf.html#setNumReduceTasks(int)
[google-results]: https://www.google.com/search?q=hdfs+merge+single+file
[getmerge1]: http://stackoverflow.com/questions/5700068/merge-output-files-after-reduce-phase
[getmerge2]: http://stackoverflow.com/questions/3548259/merging-multiple-files-into-one-within-hadoop
[getmerge3]: https://www.safaribooksonline.com/library/view/hadoop-mapreduce-cookbook/9781849517287/ch02s11.html
[org.apache.hadoop.fs.FileSystem]: https://hadoop.apache.org/docs/r2.2.0/api/org/apache/hadoop/fs/FileSystem.html
[org.apache.hadoop.fs.FileSystem.concat]: https://hadoop.apache.org/docs/r2.2.0/api/org/apache/hadoop/fs/FileSystem.html#concat%28org.apache.hadoop.fs.Path,%20org.apache.hadoop.fs.Path%5B%5D%29
[sources-removed]: https://github.com/apache/hadoop/blob/release-2.2.0/hadoop-hdfs-project/hadoop-hdfs/src/main/java/org/apache/hadoop/hdfs/DFSClient.java#L1566
[same-directory]: https://github.com/apache/hadoop/blob/release-2.2.0/hadoop-hdfs-project/hadoop-hdfs/src/main/java/org/apache/hadoop/hdfs/server/namenode/FSNamesystem.java#L1580
[must-exist]: https://github.com/apache/hadoop/blob/release-2.2.0/hadoop-hdfs-project/hadoop-hdfs/src/main/java/org/apache/hadoop/hdfs/server/namenode/FSNamesystem.java#L1633
[must-not-be-empty]: https://github.com/apache/hadoop/blob/release-2.2.0/hadoop-hdfs-project/hadoop-hdfs/src/main/java/org/apache/hadoop/hdfs/server/namenode/FSNamesystem.java#L1639
[must-have-last-block-full]: https://github.com/apache/hadoop/blob/release-2.2.0/hadoop-hdfs-project/hadoop-hdfs/src/main/java/org/apache/hadoop/hdfs/server/namenode/FSNamesystem.java#L1654
[HDFS-6641]: https://issues.apache.org/jira/browse/HDFS-6641
[HDFS-7800]: https://issues.apache.org/jira/browse/HDFS-7800
