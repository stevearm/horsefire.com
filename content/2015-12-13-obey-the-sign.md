Title: Signs, signs, everywhere a sign
Date: 2015-12-13T01:12
Tags: internet, law, disobedience

I'd like to talk about social conventions for web use, and what's allowed and not allowed. I've been meaning to write this post for a while. It's been on my list long enough that the legal saga I'm referencing has been done since April 2014.

The basic topic is about where we draw the line between legal and illegal behaviour around sending HTTP requests to a web server. At what point does an HTTP request become "illegal" or "unauthorized" considering the server is able to return whatever it wants? Should I be expected to know what actions are considered allowed by the owner of the server, or should I be allowed to rely on the meaning of the HTTP response codes as though they were posted signs on the server telling me exactly what is allowed and what is not.

# Weev vs AT&T

In June 2010, Andrew "Weev" Auernheimer helped discover that AT&T had an HTTP endpoint that, given a serial number for an iPad, would return the subscriber's e-mail address. The endpoint did not require any passwords. Weev had found a pattern allowing him to predict serial numbers, so he wrote a script that would iterate through lots of them, requesting subscriber e-mails for each one. He accumulated over 100,000 addresses, which he then gave to Gawker. An [FBI investigation][weev-fbi-investigation] led to him being [charged with conspiracy to access a computer without authorization][weev-charged] in Jan 2011. In November 2012 he was [found guilty][weev-convicted] and soon after sentenced to 41 months in prison and $73k in restitution. In April 2014 [he was released from jail][weev-released] after an appeals court overturned his conviction. It wasn't on anything relating to what I'm discussing, rather it was a technicality about what state the court case had happened in.

Let me be clear: Andrew "Weev" Auernheimer is a total bag of dicks. He is a racist, sexist waste of a human being. When Kathy Sierra spoke out against the problem of violence against women, especially online and in tech, he [released her home address and social security number][weev-vs-sierra] and engaged in a campaign of lies and threats, driving her from her home for fear of her life. I'd be happy if he was rotting in jail forever, but it should be for these death threats, or any of his other crap, not for this AT&T web scraping issue.

Mr Griffin once said ["While I may not agree with what you say, I'll defend to the death your right to say it"][family-guy-free-speech] (I think he was copied by Voltaire, or more accuratly [Beatrice Evelyn Hall][beatrice-hall]). On the same note, while Auernheimer might be a dirt bag and the worst example of someone worth defending, his actions in the AT&T case should not put him in jail.

# What is "authorization" for computers?

The Washington Post wrote an article talking about why [Weev's actions shouldn't be criminal][washington-post-weev-should-be-free] because they can't be considered to be unauthorized. The HTTP standard defines a [status code (401)][http-401] that servers can use if a request is considered unauthorized. They can require passwords. When you send a request, the server can choose to return or not return data. There is no coercion or force involved, so if the server does not ask who the request came from, and returns the data, how can the requester be considered to have committed a crime.

The [Hacker News thread about the Washington Post article][hacker-news-weev-thread] brings up that internet law usually works on physical-world analogies, since there are legal precedents for many situations in the physical world to draw from. The thread also has a ton of analogies, some I agree with and some I don't. One problem with many of them is they use public vs private property (street vs house). The internet is entirely private property. There is no [commons][commons] as we normally think of it. Physical analogies to browsing the internet should not be "walking around a public street" but "walking around a mall". It's a publicly accessible private commercial space owned by a group of companies, not a public space owned by society or the government. In that vein, I'd like to suggest an analogy that I think works better.

Let's say I brought my iPad into an Apple store to get repaired. The Apple employee phones an AT&T number, says "Can I have the e-mail address for serial number 983459238457?", the person on the other end of the line gives my e-mail address, and they hang up. The employee was never asked "Are you an Apple employee" or "Do you own that iPad" or "What is your password" or "What is your name". I then go home, call that same AT&T number, ask for a made-up serial number, and am given an e-mail address. I never lied about who I was or threatened the phone operator or coerced them to give me the info. Have I committed a crime? I say no. I simply called a phone number (not a crime) and asked a question (not a crime) and the idiot on the end of the line told me the answers.

In that example, does it matter if I tell my friends about what a crappy system AT&T has set up? Does it matter if I laugh about how poor AT&T's privacy policies are? Does it matter if I think that AT&T should have their employees asking more info of the people calling that number? Does it matter if I guess that AT&T does not want me to have this information? I still say no.

In that same example, is it a crime if I setup an auto-dialer to call the number every 10 seconds, ask for a new serial number, and record the answer. I still say no. It's not a crime to take an action many times over if the action itself is legal.

To connect this analogy back to reality, Weev found an endpoint that never asked who he was. When sent a serial number this endpoint just returned info about the serial number. This shouldn't be a crime. HTTP defines a bunch of well known response codes to allow the server to authenticate the person sending the request. None of those codes were used, so no intention or expectation of privacy or unauthorized action can be assumed.

# What about the user agent?

I've been asserting that Weev did not impersonate or lie about who was making the request (in the same way that when I make my phone call, I never lied about who I was becasue I was never asked). Weev did set the "User-Agent" header in his requests to be an iPad though. "Ah hah! Gotcha you racist bastard, you go to jail!" Well, yes and no, but mostly no.

In theory the "User-Agent" header says what program is making the request by specifying "Chrome" or "Firefox" or "Safari". In practice, pretty much since the start of the web, every single program has lied about it. Chrome identifies itself as Safari AND Chrome. Safari identifies as Firefox, and every browser since Netscape says that it's Netscape. In that light, I don't think anyone can reasonably apply concepts of authorization to this header.

My phone call analogy stretches at this point, but let's say that when you got a phone call, it said if the person calling you was a cell phone or land line. Every single phone has a dial where you can choose if you want to show as a land line or a cell phone. People switch it randomly, and for years now, noone bothers to look at what device is calling because everyone knows it's inaccurate. If the AT&T number will only answer if I call them from a cell phone, and I called from a land-line with the dial set to show cell phone, does that make it a crime? I still say no, if the social norm for decades has been that everyone switches their dial all the time.

# Can criminal intent make an action a crime?
One thing that the Hacker News thread brings up many times is Weev's intent. They argue that Weev clearly knew that AT&T didn't want this info to be publicly accesible, and he intended to get it anyways, so he committed a crime. Not bring a lawyer, it's tough to be sure I'm arguing how an under-specified part of the law works, and not how I wish a completely established part should work. That said, I think there are many cases where actions that are not criminal do not become criminal just by intent. It seems to work the other way, in that a criminal act may be dealt with more leniently if the intent was not criminal. Running over someone with my car intentionally vs accidentally are two different charges with different punishments, but in both cases running over someone with my car is inherently a crime.

Some examples and counter-examples come to mind. On the one hand, let's say I walk into a bank and ask the clerk if I can have some free money, and he/she gives it to me. Clearly I was not "authorized" to take the money, but I was given it without misrepresenting myself or coercing or threatening the clerk in any way. If I knew that one of the clerks had been trained wrong, and was giving out free money even though they shouldn't, then I knew I wasn't "supposed to" get the money. Does this knowlege make the action of asking the clerk for money a crime?

On the other hand, the charge of "attempted murder" is all about intent. If I plan to murder someone, (legally) buy a gun, and drive to their house, but stop at that point, am I liable for attempted murder? Or does that charge only come into play when I've already assaulted them during my attempt? If that's true, then this supports my point, where the crime was based on a criminal action (assault) and intent only determined how severely the action was punished (something like criminal negligence if I attacked them by accident, or attempted murder if I attacked them in order to kill them).

Obviously I need to talk to a real lawyer or do a lot more research to determine if an action can be considered criminal or non-criminal based on intent. The attempted murder example would lead to the simple question: What actions need to be proven to have been taken before someone can be found guilty of attempted murder? If a criminal action is required, I'm right. If not, I'm wrong.

# Obey the signs on the door, not the unknown wishes of the owner of the door

In the physical world, if I walk through a door with a sign that says "Come in, we're open", I'm not trespassing. If the door says "Authorized entry only", then I'm trespassing. If the door says "Come in, we're open" but the owner is not there, and it's night time, should I somehow know that the owner doesn't want me there, or can I be held to what the words on the door say?

On the internet, HTTP is an established protocol for how web servers and people's browsers/phones/computers communicate. There are codes to use for "Do not ask for this page again", "You are not authorized to view this page", and "Here's the page, your request was perfectly fine". In Weev's case, the server kept responding with the last option: "Your request was fine". If that's the case, how can he have committed a crime?

[weev-fbi-investigation]: http://www.wsj.com/articles/SB10001424052748704312104575299111189853840
[weev-charged]: http://www.computerworld.com/article/2512476/technology-law-regulation/criminal-charges-filed-against-at-t-ipad-attackers.html
[weev-convicted]: http://www.wired.com/2012/11/att-hacker-found-guilty/
[weev-released]: http://www.bloomberg.com/news/articles/2014-04-14/at-t-hacker-weev-wants-indictment-tossed-after-prison-release
[weev-vs-sierra]: http://www.theverge.com/2013/9/12/4693710/the-end-of-kindness-weev-and-the-cult-of-the-angry-young-man
[family-guy-free-speech]: https://www.youtube.com/watch?v=eMF5MjzgJrM
[beatrice-hall]: https://en.wikipedia.org/wiki/Evelyn_Beatrice_Hall
[washington-post-weev-should-be-free]: https://www.washingtonpost.com/news/the-switch/wp/2013/09/23/this-hacker-might-seem-shady-but-throwing-him-in-jail-is-bad-for-everyone/
[http-401]: http://www.w3.org/Protocols/rfc2616/rfc2616-sec10.html#sec10.4.2
[hacker-news-weev-thread]: https://news.ycombinator.com/item?id=6434400
[commons]: https://en.wikipedia.org/wiki/Commons
