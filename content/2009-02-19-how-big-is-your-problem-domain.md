Title: How big is your problem domain?
Date: 2009-02-19T20:00:00
Tags: debugging

When you're programming, debugging is just *fixing what went wrong*. It's pretty easy to start assuming, right or wrong, where the problem came from. One of the things you gain with greater experience (general experience, and more importantly experience with the relevant technologies) is better accuracy on these assumptions. It's important to always be aware of your blind spots, however. The more confident you are that different areas of a project can't interfere with each other, the greater chance you could ignore a clue to the real problem.

Recently at work, I had a situation like this. Our GWT application wasn't loading the CSS file. The file was there in the folder, and using Firebug's Net tab, I could see that the file was being loaded, but it wasn't being used by the browser, and Firebug's HTML tab didn't have any link tags for it. If it's being loaded, why isn't it in the HTML, and since it's not, how was it ever loaded?

It was showing up Firebug's DOM tab showed the css file with a variable called `__gwt_stylesLoaded`, and so I looked around Google for a while to figure out what this variable was for.

There was also talk about the difference between including the CSS file in the module's gwt.xml file, versus hard-coding the CSS link into the HTML file that loads the page. We had switched from hard-coding to gwt.xml a while ago because of some inheritance issues, and we were wondering if that was the problem. We knew that switching it back to a hard-coded system would fix the problem, but that would break the inheritance issue that made us switch in the first place.

During all of this, I was sure my small change in the loder HTML page couldn't have caused this. We use GWT on low bandwidth, high latency links, and so the html page that loads the GWT javascript files has some hard-coded "please wait" language.

index.html

    <html>
    <body>
      <div id="loadingInfo">
        <div>
          Please wait
          <div>
            We are currently loading files
          <div>
        </div>
      </div>
      <script language="javascript"
              src="myModule.nocache.js">
      </script>
    </body>
    </html>

In the EntryPoint class, the first thing we do is delete the `pleaseWait` div. This has worked well for a while, and I was just updating the look of that "please wait" section. Since the problem was that GWT didn't seem to be adding the CSS file, I saw no way my changes could affect it.

Running out of ideas, I did what I should have done in the first place: Use SVN and roll back trunk until the problem was fixed, and find exactly what commit caused the problem. Within 10 min I knew it was my commit, and 20 min of debugging showed me the problem: I wasn't closing a tag.

Look at the div that's an opening tag instead of a closing one in the posted `index.html` page. This is a simple HTML problem at first, but at the bottom of the page, we link in the javascript file for GWT. Once GWT loads, it injects a link tag for the CSS files, which makes the browser load them, and then it calls the EntryPoint class to start up the GUI. Our first action is to delete the 'pleaseWait' div. At this point, my broken HTML causes everything to be deleted from the start of the `pleaseWait` div until the `</body>`. This deletes the script tag including the GWT, but since it's already been parsed into the javascript VM, it's still kind of there. The CSS file, however, is removed from the DOM, so the browser stops caring about it.

I'm learning (admittedly slowly) that these kind of strange problems happen pretty often. I guess if the bug made sense, it wouldn't stay a bug long, and we wouldn't remember it. I assumed that my edits couldn't have been the issue because I couldn't see a way for them to interfere. These kind of assumptions can waste time, and with source control readily available (if you're not using source control, you've hobbled yourself for no reason) there's no reason that your first step shouldn't be to roll back and find the guilty commit.
