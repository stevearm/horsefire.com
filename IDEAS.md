# Undeveloped ideas / news

This file exists only to throw down links or one-liners for things that might be worth reading about

* HTTP3 is being standardized to mean HTTP + [QUIC](https://www.chromium.org/quic) + TLS. It has connection migration, so does that mean I can do a terrible reflection attack?
    1. Do an initial handshake as myself to an innocent bystander server, which requires multiple round-trips
    1. Send a fake GET "from" my target's IP using my session id. If this doesn't require a round-trip, it will end up streaming the full response to my target
* A Lebanese ISP is setting itself up to [man-in-the-middle](http://security.stackexchange.com/questions/80662/i-cant-access-websites-that-use-https-instead-getting-the-message-your-connec) all it's customer's traffic
* Python 2.7's argparse does not work correctly with subparsers. If you define `--verbose` on the top level, and have a subparser for `run`, then running `script.py run --verbose` will fail. http://bugs.python.org/issue9253
* [Software ethics](http://benlog.com/2015/05/23/the-responsibility-we-have-as-software-engineers/) - Should we have a Hippicratic Oath equivalent? Engineers don't trust computers, but "ask the computer, the computer knows and is always right" is a bad road. The computer knows nothing, it just gathers people's opinions. "Ask the computer" means "tell the computer to ask 1000 people and show the most frequent answers"
* Estonia's capital Tallinn is the [ultimate example of e-government](http://www.spiegel.de/international/europe/europe-s-coolest-cities-tallinn-estonia-s-wired-capital-a-502322.html)
* [Canada Post suing a website that provides postal codes](http://geocoder.ca/?sued=1) - [Michael Geist article](http://www.michaelgeist.ca/content/view/6415/125/)
* [Black box recording everything your car does](http://news.ycombinator.com/item?id=3863343) - Why is this not a bigger deal?
* Expand on the talk I had with Colleen regarding paranoia/tinfoil-hats with reference to DNA databanks, identity theft, and putting things out in the world about yourself that can't be taken back (DNA)

Distributed web
* What is [MaidSafe](https://en.wikipedia.org/wiki/MaidSafe#Self-Encrypted_Data)?

Misc
* Write a response to [Steve Yegge](http://steve.yegge.googlepages.com/ten-predictions) (write my own predictions as an exercise)
* Write a short blog post talking about chilling effects of surveillance. This is mostly to provide a link page for things I want to remember
  * Use [Ben's letter](http://benlog.com/2013/08/19/letter-to-president-obama-on-surveillance-and-freedom/) as a template/reference, and maybe explicitly reference it
  * Talk about [Groklaw closing](http://www.theguardian.com/technology/2013/aug/20/groklaw-shuts-nsa-surveillance) ([discussion](https://news.ycombinator.com/item?id=6243081)) ([better discussion](https://news.ycombinator.com/item?id=6242569))
  * [metadata from gmail](http://www.npr.org/blogs/alltechconsidered/2013/08/22/214172709/how-a-look-at-your-gmail-reveals-the-power-of-metadata)
* Interesting comment about [enforcing the letter of the law vs the goal the law intended to produce](https://news.ycombinator.com/item?id=5668360) (from [a post about licence plate readers](https://news.ycombinator.com/item?id=5667911))
