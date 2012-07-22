---
categories: debugging, java
date: 2009/08/10 21:24:00
title: Another rabbit hole
---
In the interest of making a post (I haven't for a long time), here's another debugging wild goose chase, and how making assumptions was the wrong thing to do (a lesson I should have learned [earlier](/blog/2009/02/19/how-big-is-your-problem-domain-/).

We make a physical product at work (among other things). It has a PPC chip on it that runs Linux, on which we run our application. Our app is written in Java, contains a web server (Jetty), and uses GWT for it's user interface. To get Java running on the device, we use GCJ to compile everything into a binary. With all these layers, most of which are either in-house software or seldom-used open source software, there's a lot of unknown interactions. And nothing brings every single piece of the chain into question like general problems such as "it's running too slow" or, in my case: "it's leaking memory".

Oh great.

Memory leaks in our world can be real leaks (problems in GCJ's C/C++ implementation of the java spec), or fake leaks, which aren't leaks exactly, but just somewhere in Java we're holding onto objects so the garbage collector can't take them. Using some logging, we determined that Java's heap wasn't growing, but linux's memory footprint for the GCJ process was, so that pointed to a leak in GCJ. Using huristic approches (watch the logs while we exercise different parts of the software) we determined that the leak happens during GWT RPC calls where we return an object. Returning any primitives didn't seem to cause a problem.

Oh sh**

We use GWT RPCs everywhere, so if they're broken, this is bad. The GWT RPC mechanism at this point was sorcery to me. I could understand how to use it, and what most of the limitations were, but I hadn't looked into exactly how the `RemoteServiceServlet` serialized a Java object to the generated javascript code. I assumed it used java's reflection. And upon looking into it, the whole thing used reflection. Since our software only used reflection once on startup, a small leak in one of the reflection APIs might exist and not have been noticed until now.

Now that I'm writing this, another of our products that ran on the same GCJ toolchain used ActionServlet (I think that's Struts) for it's webui, so that uses some reflection, but maybe not the same way as what GWT RPCs do.

So I started digging further, tested out some code paths in isolation, and noticed this method on `RemoteServiceServlet`:

    protected boolean shouldCompressResponse(HttpServletRequest, HttpServletResponse, String)

Any complex data type would be compressed, but a primitive wouldn't, because it was small enough. To remove any difference between the two cases, I overrode this to be false. Bam, the memory leak went away. I overrode this to be true, and the memory leaked regardless of what the RPC was returning. Java reflection was fine, it was GCJ's gzip implementation.

After that, a coworker (a local guru) and I looked through GCJ's source to find and fix the memory leak. I had almost written off the compression as being outside of the problem domain because by that point I was relatively sure that it was reflection, and I was about to head off for a day or so making and running some specialized test cases. Hopefully after learning the lesson twice, I'll be more resistant to the same mistake next time.
