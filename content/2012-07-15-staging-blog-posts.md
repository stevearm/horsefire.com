Title: Staging blog posts
Date: 2012-05-15T11:55:00
Tags: meta

So obviously I haven't done much posting since my [last update](/blog/2012/04/17/reclaiming-my-blog/). I may have 'upgraded' the way I write the blog, but it didn't change how much time I have or how often I have a post I want to write. So it goes.

I'm working on making the process even better though, mostly so that then I can transplant it to [another blog](http://blog.steveandcolleen.com). So far, I've got a script that will export a markdown file to an html staging file that contains the markdown and renders it using [showdown.js](https://github.com/coreyti/showdown/). This means I can then edit the staging file using any text editor, save and refresh to see how the blogofile-rendered page will look. The script can then extract the markdown from the staging file back to a markdown file, to be source controlled and deployed as normal.

The takeaway of this is: I can edit the blog offline on any computer with Dropbox and a text editor, and see how it will look. I can then deploy the new post from my own computer whenever I have internet access.

The problem is images.

Small: ![Test Image]({filename}images/2012/2012-07-15-DSCN0291.JPG){.post-image-small}

Medium: ![Test Image]({filename}images/2012/2012-07-15-DSCN0291.JPG){.post-image-medium}

Large: ![Test Image]({filename}images/2012/2012-07-15-DSCN0291.JPG){.post-image-large}

If I'm out travelling with my laptop but have no internet (while sitting on a train or during a long drive), I want to be able to write the blog post locally, and add in photos I just took. This will require that:

* The staging file allows some kind of image tag to local files
* The staging file has CSS to let me set the size of the image
* The Blogofile build resizes the image to the desired size, and copies it somewhere
* The Blogofile build edits the image path in the blog post to reference the new image location
* The Blogofile build could also make the image a link to a larger sized image

The image above was 2.6MB originally, and displayed in the staging file as the right size simply by setting the display height and width. If you're seeing it on the web, it should be displaying "native size" since the build should have resized the file to not waste bandwidth.

<sub>This post was written before any of the image stuff worked as a way to test it. If you can see the image, it means I got everything working. Horay!</sub>
