Title: Http caching
Tags: http, caching, squid
Status: draft

Squid (and really any caching proxy) is a fantastic idea. Put a server between the internet and your web server, set it up as a caching proxy, and it'll "protect" your server from the load of any duplicate requests. All your server needs to do is tell squid what's safe to cache, and what isn't. That means understanding [HTTP's cache headers|http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.1]. I've had to look this up too many times, so here is my attempt at a summary that will help me get up to speed next time I need to fiddle with them.

## Basic concept
The cache is allowed to cache a successful response, and as long as it is *fresh*, it can return the same response to the next client. If it's *stale* the cache should revalidate using an If-Modified-Since request. If nothing is explicit, then cachability and freshness is determined through arcane sorcery that involves sacrificing 100 virgins and something called "the unsundering". So let's be explicit.

## Explicit
For HTTP 1.0, the entry is fresh until the date specifed with the Expires header, like so:

    Expires: Thu, 01 Dec 1994 16:00:00 GMT

For HTTP 1.1, you can instead use a delta instead of an exact date:

    Cache-Control: max-age=86400

In general, if a cache has a fresh entry, it serves it up. If it's stale, it will revalidate usually, but in some special cases, it can serve stale entries. must-revalidate stops those special cases.
http://stackoverflow.com/questions/7573466/is-cache-controlmust-revalidate-obliging-to-validate-all-requests-or-just-the

HTTP 1.0 uses Expires. This is an absolute date.
HTTP 1.1 uses Cache-control with "max-age=x" with x in seconds. This is a delta, starting from the timestamp when the file was retrieved. This is more convenient than Expires when you think of static resources (don't have to do a calculation to serve it up). If you're in a dynamic environment, you can just as easily set Expires to current time + x, and also set max-age to x.

Notes
=====
http://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html#sec14.9.1