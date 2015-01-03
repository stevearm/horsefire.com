Title: Saving the world through metrics
Date: 2012-07-28T21:02:00
Tags: quantitative self, metrics

I love charts. They explain things so well. I wish I could have a chart that tells me how long I spend walking every day, or how many calories I eat averaged out by hour and compared to my energy level. In Star Trek, they've got amazing medicine because they're in the future. The way I've always seen it is that the [tricorder](http://en.wikipedia.org/wiki/Tricorder) gives them all the info they could want about a person's body, and better medicine follows naturally from that. I've always kind of believed that if I just had enough data, I could find the answers to all of my problems. If I could just compile a data set with the right stats, I could create visualizations of how everything works, and from there I would tweak things. The blocker is: where do I get that data set?

When you're administering a web server, you've got tons of log files and statistics you can derive information from. There are piles of data for you to sift through if you want to know

* which urls are being hit
* what browser
* what's the load on the server
* hard drive temperature
* your innermost fears
* memory usage

they're all there. Throw them all on a graph, compare, put an alarm for when they go over a certain level, whatever. My body and my life, however, don't have automatic stats. There's nothing running that writes a log message very time I sneeze. I can't get my current blood sugar level with a quick command the way I can see the current disk usage of my server. The digital world lends itself naturally to having too much data, but the physical world requires physical devices to measure data, and that costs effort or money or both. I was willing to put in some effort though, especially if it would save me money, so I got started.

##Creating Lifetracker

I decided that, even though I wasn't sure what analysis I wanted to do, more data is always better. Based on this premise, I designed something that would make it easy to record data. Any data.

I no longer had a palm pilot, but my phone was a [Blackberry Pearl](http://en.wikipedia.org/wiki/BlackBerry_Pearl). I was too cheap to pay for a data plan, so a web page was out, but it ran JavaME apps. I threw something together that, given the following text file

    1:Start work
    2:Buy food:Text,where,Where:Price,cost,Cost
    3:End work

it would create a UI. I could punch numbers to select options, and fill in fields if they were defined. Buying food would give me 2 text fields, and record a record like this

    2:1248750433672:McDonalds:4.88

I started gathering data. Given that I didn't know what data I'd need, I recorded simple things like, when I arrived at work, when I bought lunch, and for how much. The result was that I gathered a bunch of data that I didn't know what to do with, and abandoned use of the program after a couple of months.

##The idea lives on
For years, I still had a vague notion that a program or webpage that made it easy to record events would be the key. It would have to let the user record any free-form event data without much preparation. Ideally, I should be able to manually write down

* The time I got up this morning
* The distance I cycled at the gym
* The food I ate for lunch and the amount I paid for it

and tomorrow when I go to write down the time I woke up, it should auto-complete to make it easier. There's a lot of hand waving here, but it seemed like it'd be possible and handy.

##Enter CouchDB
A solution based on one of the no-SQL databases would probalby make the most sense, and [CouchDB](http://couchdb.apache.org/) had the nice feature that it could serve a whole webpage, and synced between different DB instances easily. This meant if I built a CouchApp version of LifeTracker, I could run anywhere that CouchDB could run, and even without internet (if running on my laptop while on a road trip) it would still work, and seamlessly re-sync once internet was restored.

I created a new iteration of [LifeTracker](https://github.com/stevearm/lifetracker-couchdb) and threw it up on a free [IrisCouch](http://www.iriscouch.com/) account so I could record events from any computer with internet access. I installed CouchDB on my laptop as well, and synced the databases, so now I can record events on the road (and analyze my data on the road as well).

My stomach had been hurting, so I started recording all kinds of data about what I was eating, using the new interface that would auto-complete everything based on previous events of the same type. The friction had gone down on recording data, but the simple act of writing down my foods made me aware enough my diet that I nailed down what I shouldn't eat (milk), so I never really analyzed the data.

##What now
I still think that LifeTracker has a place in my life. If I start a project, or a budget, I can use it to keep track of some basic events to later analyze. Once I've got a statistic that I can plot, I can try and change my habits and watch it trend down (or up, depending on what it is).

For now though, I'm going to try and hold off on build another iteration unless I can come up with a concrete use for the data. The analysis should be the goal, with the tool and the data being a means to an end. I'll stop treating the data as a goal in itself.

I do still believe that the data will enable some fantastic analysis though. Analytics will make my life better one day, I just need to take this:

1. Record lots of data
2. Analyze the data
3. Learn **X** about my habits
4. Fix my bad habit
5. Iterate again and again

and fill in the **X** before I start recording data, because starting the collection without speccing out the analysis (cart-horse) probably means I won't have the right data when I go to learn something.
