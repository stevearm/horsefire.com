Title: Proof of presence
Date: 2015-12-12T15:31
Tags: distributed web

In my [last post][everybit-post], I mentioned that [EveryBit][everybit] has suggested a [proof-of-presence][proof-of-presence] system to handle some of the problems that the proof-of-work system in Bitcoin solves. It is intriging, but either I'm missing something, or the whitepaper does not give a full description, so I'll explore it more here to see if I can figure out how the actual implementation would truly work.

## Bitcoin primer
Bitcoin's system is pretty elegant, but relies on a huge amount of work being done as a limiter on the ability for someone to generate fraudulent data. Bitcoin's blockchain is an ordered list of blocks, and each block contains a bunch of transactions. Each block has a checksum with magic bits that take a while to generate. Once you have the previous completed block, and a list of transactions going into the current block, you can start trying to generate the magic bits to finish the current block. Whoever in the network finds the magic bits first broadcasts them, and everyone uses that new block as the "last block" and moves onto trying to generate the next block.

The blockchain's "chain" characteristic (where a block's validity depends on the previous block) means that changing a transaction requires re-solving a block, which requires re-solving all blocks after that. The work involved in solving a block, and the fact that all other nodes in the network are busy solving the newest block in the chain, means that you would have to have more compute capacity working on your forked chain than working on the main chain. This is pretty good protection if there are lots of nodes. To incentivize nodes to stay in the network, free money is generated with each block, and given to the node who solved the block (any transactions that designated fees will also assign the fees to the node who solves the block). This financial incentive keeps a robust network of nodes online at any given time.

The consensus required (agreeing which transactions have been added to the blockchain) happens kind of as a side-effect. Nodes are always screaming along, adding transactions to the current block, solving it, and moving onto the next block. The result is the network agrees on the previous links in the chain, with the current one (and potentially the previous one if it is very recent) still being up for grabs.

## Proof of presence instead of proof of work

The proof of presence system described in the [EveryBit whitepaper][proof-of-presence] only solves the distributed membership problem. It provides a decentralized way for a group of nodes to determine membership for the next iteration based on proof of membership in previous iterations. Without the work naturally limiting block creation in a proof-of-work (PoW) system, a proof-of-presence (PoP) system would have to establish arbitrarily-timed iterations.

While PoP does not directly solve the consensus problem, if membership was established for each iteration of the group, then simple voting could be used. At the start of an iteration, all members would send out a signed vote. At the end, all members would send out a signed list of everyone's signed votes. This would establish proof that everyone saw all votes, leaving no way for extra votes to be snuck in later.

I'm still not sure if forked chains are possible in a PoP system in the same way that PoW can get them. For Bitcoin, the clients always just choose the longest chain (the one with the most blocks). In a PoP world, each side of the fork would presumably be the same length since they are time-bound, not work-bound. A system would have to be worked out to deterministically choose one of the chains.

The system that limited the number of agents allowed in the group would need to have a small growth rate. Agents will drop out, so new agent keys need to be distributed out at some prescribed rate. The system for assigning new agents would have to be carefully designed to keep agent keys from piling up in an unbalanced way, as this could centralize control in a few actors' hands, allowing for collusion.

## Proof of Presence Presents Promising Panacea

This system might work to keep something like Bitcoin working without having all the wasted hashing effort. Instead of a cottage industry that has sprung up around CPU, then GPU, then FPGA and now ASIC hashing systems, uptime and connectivity would be paramount to benefitting from being part of the network. I think it is worth persuing as a handy tool when trying to create one of these distributed networking systems like [IPFS][IPFS] or [EveryBit][everybit].

[everybit-post]: /blog/2015/11/11/everybit/
[everybit]: https://www.everybit.com/
[proof-of-presence]: https://github.com/EveryBit-com/everybit.js/blob/15b4b54e55e8491d81ac4f95ffd9beb7930522e0/whitepaper/README.md#proofofpresence
[IPFS]: https://ipfs.io/
