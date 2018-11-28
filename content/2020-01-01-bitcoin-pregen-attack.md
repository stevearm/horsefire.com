Title: Bitcoin pregeneration attack
Date: 2020-01-01T01:01
Tags: bitcoin, security, distributed web

While I was analyzing a [proof-of-presence system in my last post][pop-post], I talked a bit about Bitcoin (to contrast its proof-of-work system). During that research, I came up with an idea for a possible attack. With the financial incentive to exploit the system and the amount of people working on bitcoin, I assume if this was a true flaw it would have been found by now, but I'll lay it out anyways until I can learn a bunch more on how the checksum code and transation selection works.

## Original idea
Given that a block is solved if I can find the magic bits to add that make the checksum equal 0, if I can know the inputs ahead of time, I can pre-generate the whole block. The inputs are:
* The previous block
* All transactions
* My public key or my account (something to claim the free money that appears with each block generated)
* Some kind of signature, probably based on my private key

This means no one can start trying to solve a block until the previous one appears, and enough transactions are waiting that we have a full block. In the case where there are not yet enough transactions to fill a block, could I generate a bunch of my own transactions to get started early? If so, could I take it one step further to fill an entire block with my own transactions? If I do that, where in the checksum algorithm does the previous block go? Can I do some pregeneration if I already know everything except the previous block, so that as soon as the previous block appears I have a much reduced number space to explore when looking for the magic bits?

If people stopped accepting blocks that include transactions generated by the person solving the block, the attacker could just use a bunch of anonymous accounts. Another solution would be to change the checksum algorithm to mitigate any advantage given by pregeneration. Given the givens above, I assume this attack has been though of (or even tried), and the mitigation techniques have already been put in place. Regardless, I think it'd be a good education opportunity for myself, so I'll put together a blog post in the future about it.

[pop-post]: /blog/2015/