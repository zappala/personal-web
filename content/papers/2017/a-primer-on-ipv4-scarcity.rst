A Primer on IPv4 Scarcity
########################################################

:date: 2017-02-24
:tags: ip, addresses, network layer
:slug: a-primer-on-ipv4-scarcity
:author: Daniel Zappala

Paper review: `A Primer on IPv4 Scarcity:
<http://www.sigcomm.org/sites/default/files/ccr/papers/2015/April/0000000-0000002.pdf>`__,
by Philipp Richter, Mark Allman, Randy Bush, and Vern Paxson (TU Berlin, UC Berkeley, ICSI, Internet Initiative Japan)

This paper discusses the history of IPv4 address allocation, the usage
patterns that have led to scarcity, and possible solutions for dealing
with scarcity.

The paper is a good tutorial on how addresses are allocated among registries.

Differences between legacy address allocations
  - fewer are routed

    The paper nicely points out how there is no enforcement over address allocation -- any organization could
    send BGP routes for any set of IP addresses they want, hijacking a part of the space for their own. In fact, this
    happens accidentally at times due to misconfiguration. Pointer to paper on this.

  Address markets -- addresses for sale! RIR transfers and external transfers

  Natural solution is IPv6 -- pointer to paper on this.

  Carrier-grade NAT
  More efficiency

  Research questions

    


References
==========

.. [1] 

