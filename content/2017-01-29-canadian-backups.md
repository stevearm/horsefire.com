Title: Canadian backup solutions
Date: 2017-01-29T21:38
Tags: backup, privacy

You've got a bunch of data on your computer (taxes, photos, the recipe for Aunt Maude's Ultimate Chocolate Tar). You could lose it to your hard drive dying, or to the increasingly aggressive cybercrime groups that will encode all your files and ask for $5,000 for the decode key. Or maybe you drop your laptop into the sea.

Backups are your friend no matter what goes wrong. [Dropbox](https://www.dropbox.com/) is probably your easiest solution. The free plan should hold all your documents, but maybe not pictures. If needed, you can pay for more storage space. If you're paying anyways, [Carbonite](https://www.carbonite.com/en/cloud-backup/personal/buy/) and [Backblaze](https://secure.backblaze.com/buy.htm) both have excellent reviews and are pretty cheap.

If you're Canadian though, you might care about your data being subject to US laws, and having the NSA (now under the control of an orange goblin) scoop up your files from the US datacenter where it's backed up. Many hospitals and schools in Canada are unable to use common things like Google Apps because Canadian privacy laws don't allow them to "export" other people's data to another country. Companies like Google sometimes put servers in Canada to solve this problem, but sometimes they don't consider it worth it.

What you want is a company that is:

* Low cost (or free)
* Good experience and software - You want this to "just work"
* Data storage location promise - You need to see on their website that they *explicitly* say your data will be on a Canadian server only

Nope
----
* [Carbonite](https://www.carbonite.com/) has a great user experience, but I chatted with a customer rep on yesterday and they confirmed they only have US servers.
* [Canadian Cloud Backup](http://canadiancloudbackup.com/faqs/) explicitly keeps data in Canada, but it looks like it's a B2B product so you're not going to have a good time as an end-user.
* [Microsoft OneDrive](https://onedrive.live.com/about/en-ca/plans/) is an consumer folder backup/sync thing like Dropbox. Apparently Microsoft Cloud now has [Canadian datacenters](https://www.microsoft.com/en-ca/sites/datacentre/default.aspx), but today a Microsoft rep confirmed that data locality is handled automatically and they can't promise it will stay in Canada. They a bunch of things about data on servers not being subject to policies of the region where the server resides, but from a legal perspective, that's nonsense.
* [Dropbox](https://www.dropbox.com/) is great to use, but despite [this list][Canadian-backup-list], I confirmed on 2017-02-02 that all your data is on US servers, and Dropbox (the company) has the keys. No matter how good their security is to keep an employee from reading your files, if the government orders them to hand over your files, they can, and will (because they legally have to).

Maybe
-----
* [Sync.com](https://www.sync.com/blog/a-secure-canadian-dropbox-alternative/) is explicitly styled as a Dropbox alternative. Reviews look good for consumer experience, and they use Canadian servers. Try it out using the [free 5 GB plan](https://www.sync.com/pricing/), and put your data in the *Vault* feature. The *Files* feature works like Dropbox and syncs, but a deleted file is deleted everywhere. *Vault* lets you go back 30 days, so if your computer encrypts/deletes everything, you can still go back to get the original files. They use zero-knowledge encryption (this means even they can't read your files), so if you loose your password, your backups can't be decoded. Write down your password, and make sure it's somewhere that, if your house burned down with your computer inside it, you'd still have it.
* [Backblaze](https://www.backblaze.com/) is another great user experience with good pricing. Despite [this list][Canadian-backup-list] saying they have Canadian servers, yesterday Backblaze confirmed to me they don't have, or plan to have, Canadian servers. However, their page describing [the encryption setup](https://help.backblaze.com/hc/en-us/articles/217664688-Can-you-tell-me-more-about-the-encryption-Backblaze-uses-) says that you can use your own password to encode the backups. This would mean Backblaze (and the US Government) can't decode the backups, but just like Sync.com, if you loose that password your backups are useless.
* [Eazy Backup](https://eazybackup.ca/pricing/) keeps your data in Canada, but it is a bit expensive and I have no idea how easy to use it is.

Conclusion
----------
Back your stuff up somewhere. If you are Canadian and don't want various US agencies sifting through your data, then try [Sync.com](https://www.sync.com/blog/a-secure-canadian-dropbox-alternative/). If that sucks (I haven't tried it), you can use [Backblaze](https://www.backblaze.com/), and make sure to set your own password. For either one, write down that password somewhere where you'll have it even if your house is gone or your computer got stolen.


[Canadian-backup-list]: https://www.bdc.ca/en/articles-tools/technology/free-low-cost-applications/pages/online-data-backup-free-low-cost-options.aspx
