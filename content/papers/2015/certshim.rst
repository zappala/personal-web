CertShim
########

:date: 2015-01-28
:tags: authentication, certificates
:slug: certshim
:author: Daniel Zappala

Paper review: `Securing SSL Certificate Verification through Dynamic
Linking <http://dl.acm.org/citation.cfm?id=2660338>`__, from CCS 2014
[1]_.

This paper is concerned with vulnerabilities in the SSL/TLS protocol
stack. There have been numerous advances in this area, but slow
deployment of these solutions. In addition, any new solution often
doesn't address securing existing programs.

The authors propose a new system called CertShim, which intercepts
certificate validation transparently and redirects it to their
system.  CertShim can then validate certificates using any number of
proposed schemes, such as Convergence, Certificate Pinning, or DANE.
The interception is done by providing a dynamically linked library that
supports the same calls as OpenSSL and GnuTLS, then ensuring this
library is loaded first using the Linux LD_PRELOAD environment
variable. They do some measurements to show that this supports 94% of
applications on Ubuntu.

There are some limitations to this approach: CertShim handles only
dynamically linked applications, and only those applications using a
standard library they have mocked. This has implications for
maintenance of CertShim over the long term -- any changes to a
library, or introduction of a new library, requires corresponding
changes to CertShim. 

Overall, this is a nice idea that could improve security for apps
and ease deployment for new authentication systems.

References
==========

.. [1] Adam Bates, Joe Pletcher, Tyler Nichols, Braden Hollembaek, Dave
   Tian, Kevin R.B. Butler, and Abdulrahman Alkhelaifi. 2014. Securing
   SSL Certificate Verification through Dynamic Linking. In
   Proceedings of the 2014 ACM SIGSAC Conference on Computer and
   Communications Security (CCS '14). ACM, New York, NY, USA,
   394-405. DOI=10.1145/2660267.2660338
   http://doi.acm.org/10.1145/2660267.2660338

