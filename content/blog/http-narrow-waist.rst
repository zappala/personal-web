HTTP as the Narrow Waist of the Future Internet
###############################################

:date: 2013-09-09
:tags: Internet architecture
:slug: http-narrow-waist
:author: Daniel Zappala

A variety of new Internet architectures have been proposed over the
past decade, often to explore a new feature such as improved security
or content-based networking. Any new architecture must also address
the critical issue of evolvability, since we can't hope to perfectly
predict what services a future Internet will need. In this regard, IP
has become a bottleneck for the current Internet, since it has proven
extremely difficult to deploy even a single alternative such as IPv6
alongside it.

In a paper called `HTTP as the Narrow Waist of the Future Internet
<http://doi.acm.org/10.1145/1868447.1868453>`__, Popa et al. argue
that HTTP could be the focus of evolvability for a new Internet
architecture [1]_. Already HTTP is the protocol where new services are
most rapidly being deployed, such as video streaming and web
applications. The paper discusses the advantages of HTTP with respect
to content-centric networking, middleboxes, and data mobility. In
addition, the authors propose a new HTTP method that can be used to
provide low latency services for VoIP, chat and other real-time
applications. It is this extensibility that provides significant
advantages for HTTP over IP as a key layer in a future Internet
architecture.

The main idea of content-centric networking is that users access
content via names (ESPN or "Daniel Zappala"), rather than hosts
(espn.com or zappala.byu.edu). This allows the architecture to
separate the name of content from its location, which could be a
single server but could also be a set of content caches spread
throughout the network. The authors argue that HTTP provides a very
similar content-centric service, and that DNS can be adapted to allow
for persistence, fast updates, and security that are required of a
content-centric architecture. However, most content-centric
architectures translate names into content-centric identifiers that
are used for routing to a nearby copy, not location-centric IP
addresses. The key question for me is whether content-centric routing
offers significant benefits, given what DNS+HTTP already offers.

A key benefit of HTTP is its flexibility with regard to extensions and
support of application-layer protocols. The authors make several weak
arguments that this flexibility extends to network-layer services,
such as multicast and anycast. For example, they claim the success of
video distribution for the Olympics as evidence that HTTP can provide
large scale single-source multicast, but I would argue that the key to
making live events scale has been IP multicast to local caches. They
also claim HTTP can use DNS anycasting, but don't offer any details or
comparison to content-centric routing based on anycast.

The main contribution of the paper is the design of a new method for
HTTP that allows it to support push-oriented datagram services such as
VoIP and other real-time applications. The basic idea is that a client
sends an S-GET request for a URI to the server, which stores it and
streams all new content for the URI to the client. `Push technologies
<http://en.wikipedia.org/wiki/Push_technology>`__ have been around for
a long time, and one known as `Server-Sent events
<http://dev.w3.org/html5/eventsource/>`__ has been around since it was
implemented by Opera in 2006 and is now being standardized for
HTML5. It's disappointing this wasn't discussed by the authors.

The authors acknowledge several other weaknesses of HTTP with respect to an
improved Internet architecture: it has limited support for QoS
guarantees, is vulnerable to network-layer DoS attacks, has poor
naming persistence, and has higher overhead than IP. With improving
bandwidth and the use of DASH for video, I am less concerned with QoS
support, but these other weaknesses are significant and are left for
future work.


References
==========

.. [1] Lucian Popa, Ali Ghodsi, and Ion Stoica. 2010. HTTP as the
  narrow waist of the future internet. In Proceedings of the 9th ACM
  SIGCOMM Workshop on Hot Topics in Networks (Hotnets-IX). ACM, New
  York, NY, USA, , Article 6 , 6 pages. DOI=10.1145/1868447.1868453
  http://doi.acm.org/10.1145/1868447.1868453

