---
categories: security, java
date: 2012/08/29 20:25:00
title: Disable your Java browser plugins
---
I like Java. I enjoy programming in it. As a browser language, however, it's a security nightmare. With exploits like [flashback](https://www.google.com/search?q=flashback+botnet), you should be careful about running Java in your browser.

#Test my browser
If your browser is running Java, you're at risk. Go to a [test page](http://javatester.org/enabled.html) and compare what you see with the images below:

**I am protected**

<img src="2012-08-29_java_test_disabled1.png" class="post-image-large">
<img src="2012-08-29_java_test_disabled2.png" class="post-image-large">
<img src="2012-08-29_java_test_disabled3.png" class="post-image-large">

**Oh god the viruses**

<img src="2012-08-29_java_test_enabled.png" class="post-image-large">

#Chrome
If you use Chrome, you're probably got asked a question:

<img src="2012-08-29_java_test_chrome_question.png" class="post-image-large">

If you saw that, you're safe. Feel free to click **Run this time** on a trusted website, like your bank. Stay away from that button if it pops up when you're trolling around *lolcats.haxors.ru* though.

If that yellow bar didn't pop up in Chrome, and your browser just showed the "...can indeed run Java...":

* open a new tab
* go to **chrome://plugins** (just copy-paste that into the address bar)
* find the row marked *Java*
* make sure "Always allowed" is unchecked

<img src="2012-08-29_java_test_chrome_plugin.png" class="post-image-large">

#Firefox
If Firefox displayed the "...can indeed run Java...":

* Press **Ctrl + Shift + A** (Windows) or **Command + Shift + A** (Mac)
* Go to Plugins
* Disable the "Java Deployment Toolkit" and "Java(TM) Platform" plugins

