---
categories: meta
date: 2012/04/17 10:05:00
title: Reclaiming my blog
---
Well, I'm trying to launch a new blog. I barely ever used the ready-to-go free-of-charge [Blogger](http://www.blogger.com), so I'm learning my lesson and attempting to use a mostly abandoned open source static site generator. I'm sure this will result in a more steady update schedule.

I'm using [Blogofile](http://www.blogofile.com/), which is a python static site generator. Given a directory of [Markdown](http://daringfireball.net/projects/markdown/) posts and [mako](http://www.makotemplates.org/) html templates, it will generate a fully static website. This has a number of benefits:

* All my blog posts are in flat files instead of a database, so I can put them in source control, grep through them, and back them up and restore them easier
* My posts are in Markdown, which is easier to read as source, and can be easily converted into a number of formats
* My final site is static HTML, javascript and CSS, so I can host it anywhere, even S3. No dependencies on a database, or dynamic language runtime. This means cheaper hosting, and also more scalable.

and drawbacks:

* My final site is static, so hosted comments are out. But [Disquis](http://disqus.com/) comments are integrated into Blogofile, so if I want comments, I can use that. Apparently it's not bad
* Uploading a new post or editing an existing post requires my pc with the full Blogofile stack installed
* When writing a post in Markdown, I don't have any kind of live preview without rebuilding the static site

There are some upgrades I can do to ease the drawbacks. I can put the whole blog into [github](https://github.com/), then when something new is pushed, github would trigger my hosting account to fetch a new copy of the blog, build it, and copy it to the hosted directory. This would also solve the edit problem, as github allows on-site editing of files. New files would still require a PC with git installed though. I can also whip up a live preview using one of the javascript implementations of Markdown, or for more accuracy, spin up a python server that will render the templates and markdown file on demand. Any of these improvements take time though, so they won't be done instantly.

And then there's the look. I don't like designing the look of a site, likely because I'm not good at it. Any attempt to fix the visual style of an HTML page ends up as a giant time-sink for me. This may result in my new blog being much uglier than my old blog.

In the end, my basic calculation was:

* Have all my future blog posts (and with only 4 past ones to convert) on my machine in source control - **good**
* Allow hosting on any webhost - **good**
* Full control over HTML to let me do anything - **good**
* Full control over HTML so style is now my problem - **annoying, but will force me to improve**
* Abandoned python project with missing features - **annoying, but I want to learn python, and this will make me**
* Might make blogging harder - **neutral, since I hadn't blogged for 3 years anyways**

which comes to some solid benefits, and some friction points that are only a problem because I have actual gaps in my skillset. So here goes.
