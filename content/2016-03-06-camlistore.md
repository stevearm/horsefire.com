Title: Camlistore
Date: 2016-03-06T17:20
Tags: distributed web, backup, golang

So while looking into IPFS and maybe learning go, I stumbled onto [Camlistore][camlistore]. It's a content-addressed file pile that scratches all my itches of backups, redundant storage, flexible indexable formats, etc. Watch [Brad Fitzpatrick's talk][camlistore-talk] for a great intro into the promise of the system.

The documentation is a little sparse, so as I explored I wrote down some notes. I'm posting them here for myself and others. This assumes you got it to compile and run, but now don't know what to do or how to use it.

## Data model

Permanodes are where it's at. They show up in the web ui (every icon is a permanode). Anything not a permanode will not be indexed and won't show up in the UI. It will still be backed up however, and stored until the next GC run, but since GC is not yet implemented, that run won't happen soon.

If you just want to shove a bunch of files in, have them indexed, but don't need to preserve the directory structure:

    camput file -filenodes ~/pictures

Running this again (if no files changed) will not create any more entries in camlistore.

If you want to backup (maybe periodically) a directory structure in a way that you can get it back out later, you need more. [This comment thread][backup-thread] mentions creating a single permanode and hanging each backup session off it. First create that permanode:

    PERMANODE=$(camput permanode)
    camput attr $PERMANODE title pictures
    camput attr $PERMANODE tag backup

Try `camtool describe` on any of the hashes to see what's going on. Backing up the folder now is a simple process of actually backing it up

    BACKUP=$(camput file /home/steve/pictures)

and then attaching the backup to the permanode

    camput attr $PERMANODE camliContent $BACKUP

Over time, the history of the permanode will point to a bunch of different hashes. I'm unsure of what that'll mean for GC and removing old backups of files you don't care about anymore, but I'll cross that bridge when I come to it. If we want to restore the backup, we find the current hash that the permanode points to

    camtool describe $PERMANODE

and export it

    camget -o ~/tmp $CAMLICONTENT_HASH

## Recovery support

First, I want to be sure how to get things running again if I lost a hard drive. This project is supposed to be able to reindex from a blob store if all indexes are lost.

### Local diskpacked blobstore
I tried running with the default [server-config.json]({filename}images/2016/2016-03-06/local-diskpacked.json), which has a simple blob store and a leveldb index. After putting some backups in, I deleted the leveldb folder and launched again with `camlistored -reindex` and everything came back just fine.

### S3 blobstore
I next edited [server-config.json]({filename}images/2016/2016-03-06/s3.json) to have an unencrypted s3 store. After adding the backups again, I deleted the local leveldb and sync folders, reindexed, and everything was fine.

### Encrypted S3 blobstore
The next setup is complicated enough that it needs the "real" config. The [/debug/config][local-config] page shows the low-level config that is currently being run (the simplified high-level config is used to generate in memory the low-level config). I grabbed this, edited it, and saved it as the new [server-config.json]({filename}images/2016/2016-03-06/encrypted-s3.json).

I switched out the diskpacked blobstore, and piped the normal blobstore flow instead through an encryption blobstore, then to S3. I imported some files into camlistore, turned it off, deleted all local files except for the config file, and ran with `camlistored -reindex` and it downloaded, decrypted, and reindexed everything.

### Multistore with S3
I configured the Synology to have a normal default diskpacked blobstore, and an encrypted S3 store (which was not on the normal import path). After backing up a folder on the Synology as described above, I synced the Synology's default blobstore to its S3 store. Using an empty camlistored on my laptop (which had the same S3 repo), I was able to sync from the S3 repo to the laptop's local diskpacked store, then export the same permanode backup locally on the laptop.

## My plan

I want to backup a [Lightroom][lightroom] library, and all associated RAW and processed files. I want these backups to exist on my Synology as well as in the cloud somewhere (S3 or Glacier probably). As an added wrinkle, after a day taking pictures, my wife will offload a big chunk of files into Lightroom, but might not have time for days or weeks to groom and process them all. During this time, the un-processed files should be replicated to the NAS (and possibly the cloud) to protect against data loss. Once groomed though, I don't want to forever have a backup of the deleted files (especially not in the cloud where I pay for it).

I asked this on the [mailing list][mailing-list-backup-question], and we came to the conclusion that with GC not yet implemented, there isn't a good solution for this. Perhaps I'll have time to implement (or help implement) GC sometime soon.

For now, I'll push the full backup to my NAS's normal blobstore, and sync that to S3. During times when Lightroom has lots of unprocessed stuff, I'll back up to another blobserver on the NAS (add a different blobstore that's not on the main indexed data path). That extra blobserver will not be synced to S3, and can be wiped every now and then. This solution kind of sucks, in that I'll have to have duplicated blobstores on the NAS, and backup twice, but it will get me by until GC is functional.

Camlistore looks like a neat project, and gives me a place to put random bits of code. It's an agent that can do things like:

* Pull backups down from Dreamhost for me
* Take snapshots of my personal wiki and keep it somewhere
* Automatically upload all photos to Flikr, or Google Photos, or whatever new things is available
* Have a searchable data store of all my documents, without locking into Google Docs or another provider

It looks like it has lots of promise, and is a great excuse to teach myself go.

[camlistore]: https://camlistore.org/
[camlistore-talk]: https://www.youtube.com/watch?v=kBCQq5hfsug
[backup-thread]: https://groups.google.com/forum/#!searchin/camlistore/backup/camlistore/4Ig2tug9V5s/50L6OKglJqIJ
[local-config]: http://localhost:3179/debug/config
[lightroom]: http://www.adobe.com/Lightroom
[mailing-list-backup-question]: https://groups.google.com/forum/#!topic/camlistore/8RpiSScukDc
