Title: Code highlighting on Blogger
Date: 2009-02-05T20:00:00
Tags: meta

**This blog is no londer hosted on Blogger, so while this information is likely still correct, the syntax highlighting shown is not using the method described.**

If I'm going to write about computers and programming, I'm going to be posting code snippets, and syntax highlighting is essential for reading code. Blogger doesn't have build in code highlighting, but the internet comes the rescue. [SyntaxHighlighter](http://code.google.com/p/syntaxhighlighter/) provides a nice utility to do this client side (the browser does the highlighting, not my blog software).

The manager of SyntaxHighlighter project setup an online host for the files. This means you can link directly there. Edit the template for your blog, and add the following line just before the `</head>` tag:

    <link type="text/css" rel="stylesheet" href="css/SyntaxHighlighter.css"></link>
    <script language="javascript" src="http://syntaxhighlighter.googlecode.com/svn/tags/1.5.1/Scripts/shCore.js"></script>

And for each language you want highlighted (see [here](http://syntaxhighlighter.googlecode.com/svn/tags/1.5.1/Scripts/) for the list) add another line. I just want Java, so I put:

    <script language="javascript" src="http://syntaxhighlighter.googlecode.com/svn/tags/1.5.1/Scripts/shBrushJava.js"></script>

Then add these lines just before the tag at the bottom:

    <script language="javascript">
        dp.SyntaxHighlighter.BloggerMode();
        dp.SyntaxHighlighter.HighlightAll('code');
    </script>

Here's a sample Java snippet to test that things are working. To make it work, I just encase the code in these tags:

    <pre name="code" class="java"></pre>

and I get:

    import java.awt.Graphics;

    /**
     * Example javadoc
     *
     * @author Steve
     */
    public class Hello1 extends java.applet.Applet {
      @Override
      public void paint(Graphics g) {
        // Write a greeting
        g.drawString("Hello, World!", 50, 25 );
      }
    }
