---
categories: meta
date: 2009/02/05 20:00:00
title: Code highlighting on Blogger
---
If I'm going to write about computers and programming, I'm going to be posting code snippets, and syntax highlighting is essential for reading code. Blogger doesn't have build in code highlighting, but the internet comes the rescue. [SyntaxHighlighter](http://code.google.com/p/syntaxhighlighter/) provides a nice utility to do this client side (the browser does the highlighting, not my blog software).

The manager of SyntaxHighlighter project setup an online host for the files. This means you can link directly there. Edit the template for your blog, and add the following line just before the &lt;/head&gt; tag:

<pre>
&lt;link type="text/css" rel="stylesheet" href="css/SyntaxHighlighter.css"&gt;&lt;/link&gt;
&lt;script language="javascript" src="http://syntaxhighlighter.googlecode.com/svn/tags/1.5.1/Scripts/shCore.js"&gt;&lt;/script&gt;
</pre>

And for each language you want highlighted (see [here](http://syntaxhighlighter.googlecode.com/svn/tags/1.5.1/Scripts/) for the list) add another line. I just want Java, so I put:

<pre>
&lt;script language="javascript" src="http://syntaxhighlighter.googlecode.com/svn/tags/1.5.1/Scripts/shBrushJava.js"&gt;&lt;/script&gt;
</pre>

Then add these lines just before the tag at the bottom:

<pre>
&lt;script language="javascript"&gt;
    dp.SyntaxHighlighter.BloggerMode();
    dp.SyntaxHighlighter.HighlightAll('code');
&lt;/script&gt;
</pre>

Here's a sample Java snippet to test that things are working. To make it work, I just encase the code in these tags:

<pre>
&lt;pre name="code" class="java"&gt;&lt;/pre&gt;
</pre>

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
