Title: My heart bleeds for you
Date: 2014-04-11T11:02:00
Tags: security

Security nerds come out with some good names. [BREACH](http://breachattack.com/), [CRIME](http://hackmageddon.com/2012/09/13/more-details-on-crime-attack-uses-tls-compression-video/), and now [Heartbleed](http://heartbleed.com/).

## What is it?

On March 14, 2012, OpenSSL 1.0.1 was released, which is used in many secure web sites (banks, e-mail servers, and online stores). A bug in this software allowed anyone who was watching to break the encryption. This means they can:

* See your username and password when you typed them in
* See everything else (account numbers, user info) that appeared on that site

The real unknowns are:

* Did the website I use even have the bug?
* If it did, was anyone listening at the time I logged in?

The answers are hard to find, and harder (or impossible) to be sure of.

## What do I do?

That's, unfortunately, more complicated. Some sites (Amazon, Chase, Citibank) were supposedly not using the broken software, so they were never at risk. Many, many sites were using the buggy software, but have since fixed it (Google, Yahoo), and so you should change your passwords on them. Third, some were at risk, and still haven't fixed it (American Express). There's not much point in changing your password on these ones until they fix it.

Knowing which is which is hard though. You can checkout [various articles](http://money.cnn.com/2014/04/10/technology/security/heartbleed-passwords/) that have lists, but in general, it can't hurt to [change some passwords](http://horsefire.com/blog/2012/09/22/protect-yourself-from-security-failures/) for key sites.

## That's not helpful

Yea, I know, sorry. Just about every online company is scrambling to either confirm they're immune, or to fix the gap. What they tell their users is going to vary. Hopefully you'll be getting a bunch of e-mails from various sites to change your passwords. If you get one, change it. If you don't get one in the next couple days, change your password anyways on important sites (like banking and your primary e-mail account).

While you're changing your passwords, try to create multiple different passwords so at least your banking isn't on the same password as your e-mail or your Netflix. You could even go full tinfoil-hat and [use a different password for every page](http://horsefire.com/blog/2012/09/22/protect-yourself-from-security-failures/).
