Title: Fixing the "too many open files" error
Tags: linux, debugging
Date: 2015-01-10T00:59:12

If your service is dying from a "Too many open files" error, don't increase the `nofile` limit in `/etc/security/limits.conf` like most of the internet *says*. Instead, do what most of the internet *does*, and hard-code a `ulimit -n 100000` line in your `/etc/init.d/` script.

# Discovery process

I was working on a [Kafka][kafka] problem with too many files. I looked to Cassandra for the fix, knowing that it had an increased limit.

According to most of the internet, the right way to increase the limit on open files is to edit `/etc/security/limits.conf` (or put a file in `/etc/security/limits.d/*.conf`, which does the same thing). If you do that, log out, then back in, and running `ulimit -l` will show you your new limit. Run a process, and `cat /proc/[pid]/limits` and you'll see the limits took effect. Done, right?

Nope. Set the limits for the user `cassandra` (which has no shell) just like they [recommend][cassandra-limits]. Good luck verifying that they took effect. `sudo su -s /bin/bash -c "ulimit -l"` shows your own limits. But if you run `ulimit -l` from cron.d as the `cassandra` user, it'll show the correct limits.

But the Cassandra process runs with the correct limits, so maybe it's because it uses `start-stop-daemon` instead of `su` to launch the process. Nope, apparently [start-stop-daemon][start-stop-daemon] doesn't read the limits file. Debian has an [open bug][debian-bug] with a patch to fix it. Given it's been open since 2005, I'm sure it'll be merged in soon.

So how does Cassandra start with the right file limit?

Oh, they just [hard code the limit in the init script][cassandra-init]

    FD_LIMIT=100000
    ulimit -n 100000

Cheaters. If only they admitted this in their [docs][cassandra-limits], I wouldn't have gone down the wrong path.

[kafka]: http://kafka.apache.org/
[cassandra-limits]: http://www.datastax.com/documentation/cassandra/2.0/cassandra/install/installRecommendSettings.html
[start-stop-daemon]: http://superuser.com/questions/454465/make-ulimits-work-with-start-stop-daemon
[debian-bug]: https://bugs.debian.org/cgi-bin/bugreport.cgi?bug=302079
[cassandra-init]: https://github.com/apache/cassandra/blob/c04c50c95baaf3be6c7069b3aa617a0a066cd792/debian/init#L82
