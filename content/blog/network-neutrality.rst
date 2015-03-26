Network Neutrality
###############################################

:date: 2014-11-18
:tags: network neutrality
:slug: network-neutrality
:author: Daniel Zappala

We are covering network neutrality in `CS 660 <http://cs660.byu.edu>`__
this week. This is a great topic for exploring the structure of the
Internet and business relationships among ISPS, as well as a chance to
grapple with difficult policy questions.

Network neutrality has been in the news a lot lately, with the FCC
considering whether to impose regulations. A number of articles from Vox
cover this space for the general public:

* `9 questions about network neutrality you were too embarrassed to ask <http://www.vox.com/2014/11/10/7187281/9-questions-about-network-neutrality-you-were-too-embarrassed-to-ask>`__

* `Obama's big net neutrality announcement, explained <http://www.vox.com/2014/11/10/7186179/obamas-big-net-neutrality-announcement-explained>`__

* `Beyond net neutrality The new battle for the future of the internet: <http://www.vox.com/2014/5/2/5665890/beyond-net-neutrality-the-new-battle-for-the-future-of-the-internet>`__

Network Neutrality Inference
============================

The first paper we read is from SIGCOMM 2014, titled `Network
neutrality inference
<http://dl.acm.org/citation.cfm?id=2626308>`__ [1]_. This paper constructs
a model to show the conditions where it is possible to detect network
neutrality violations, using only measurements of application
performance from endpoints. The model is based on a clever insight
from tomography, where inferences about network performance are made
using a linear system of equations. The authors make the observation
that network neutrality violations result in an unsolvable system of
equations. They use this idea to show that they are able to isolate a
single link or a sequence of links as causing a network neutrality
violation.

The following figure from the paper illustrates the model:

.. figure:: /images/network-neutrality/inference-figure1.png
  :alt: neutrality inference example network
  :width: 400px
  :figclass: figure

In this network, three applications are using paths :math:`p_1, p_2,
p_3`.  The ISP separates the traffic into two separate classes, and
treats traffic from :math:`p_2` as having lower priority than traffic
from either :math:`p_1` or :math:`p_3`.

The authors show how to split the non-neutral link :math:`l_2` into
two pieces, where :math:`l_2^+(1)` captures the performance of the
link for class 1 (:math:`{p_1,p_3}`) and :math:`l_2^+(2)` captures the
performance of the link for class 2 (:math:`{p_2}`). This is shown in
the figure below:

.. figure:: /images/network-neutrality/inference-figure3.png
  :alt: neutral equivalent
  :width: 400px
  :figclass: figure

Notice :math:`p_2` is the only path that traverses link
:math:`l_2^+(2)`, so that any performance differences can be observed
as a network neutrality violation.

The paper discusses the formal conditions for observability of network
neutrality violations and identifiability conditions for links
involved in a violation. Based on these results, it develops an
algorithm that can have no false positives but no false negatives. The
performance of the algorithm is verified using emulation on a variety
of topologies. 

ISP Interconnection and its Impact on Consumer Internet Performance
===================================================================

We next paper we read is a technical report from the `Measurement Lab
Consortium <www.measurementlab.net>`__, called `ISP Interconnection
and its Impact on Consumer Internet Performance
<http://www.measurementlab.net/static/observatory/M-Lab_Interconnection_Study_US.pdf>`__. This
report examines measurements between access ISPs (AT&T, Comcast,
Centurylink, Time Warner Cable, and Verizon) and transit ISPs (Cogent,
Level 3, and XO) in a variety of locations around the United States.
They observe performance degradations such as higher round trip times,
increased packet loss, and decreased throughput during periods of high
network use among certain pairs of access and transit ISP. The
evidence indicates that this is due to business relationships between
ISPs.

A good example of the problems observed is shown below:

.. figure:: /images/network-neutrality/interconnection-figure1.png
  :alt: download throughput for Cogent with three ISPs
  :figclass: figure

This shows the throughput between New York City customers of TWC,
Comcast, and Verizon as they connect through the Cogent transit
ISP. Notice that degradation is severe betwen June 2013 and
February 2014. It is well below 4 Mbps and as low as 1 Mbps. During
this same period, throughput between New York City customers of
Cablevision and Cogent was around 14 Mbps. Likewise, performance
between customers of all four ISPs and the Internet transit ISP had an
average throughput of 14 Mbps during the same time:

.. figure:: /images/network-neutrality/interconnection-figure3.png
  :alt: download throughput for Cogent with Cablevision
  :figclass: figure

This indicates the problem is the connection between specific access
ISPs and transit ISPs. The consequence of this problem is nicely illustrated below, where daily download speeds fall below 0.5 Mbps.

.. figure:: /images/network-neutrality/interconnection-figure4.png
  :alt: daily download throughput
  :figclass: figure

The report has numerous additional details on other metrics such as
round trip times and loss rates, as well as data from other areas of
the country. All the data and tools are open source.



References
==========

.. [1] Zhiyong Zhang, Ovidiu Mara, and Katerina
   Argyraki. 2014. Network neutrality inference. In Proceedings of the
   2014 ACM conference on SIGCOMM (SIGCOMM '14). ACM, New York, NY,
   USA, 63-74. DOI=10.1145/2619239.2626308
   http://doi.acm.org/10.1145/2619239.2626308

.. [2] Measurement Lab Consortium. 2014. Technical Report.
   http://www.measurementlab.net/static/observatory/M-Lab_Interconnection_Study_US.pdf

