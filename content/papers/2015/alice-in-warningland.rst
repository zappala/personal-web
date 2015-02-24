Alice in Warningland
####################

:date: 2015-02-18
:tags: browser warnings, usability
:slug: alice-in-warningland
:author: Daniel Zappala

Paper review: `Alice in Warningland:
A Large-Scale Field Study of Browser Security Warning Effectiveness <https://www.usenix.org/conference/usenixsecurity13/technical-sessions/presentation/akhawe>`__, by Devdatta Akhawe (University of California, Berkeley) and Adrienne Porter Felt (Google, Inc.), from CCS 2014 [1]_.

This paper makes the argument that browser warnings can be designed in
a way that helps users heed the warnings and avoid clicking through
them. Naturally, the effectiveness of a warning varies based on how the
warning is designed.

This paper follows on a rich history of prior work that used lab
studies to show that users mostly ignore browser warnings and click
through them.  However, since these studies were performed, browser
warnings have been significantly redesigned, so that they are now full
page instead of relying on a relatively small security indicator. In
addition, prior work has mostly relied on lab studies, which can
inflate clickthrough rates because participants may feel safer when
conducting a study than when they are using their own computer in a
natural setting.

The major contribution of Alice in Warningland is a large-scale field
study of browser warnings in both Firefox and Chrome, using telemetry
data collected anonymously from users who have opted in to the
program. This enables the authors to study over 25 million warning
impressions, measuring how many click through, how many leave, and the
time spent examining the warning. Overall, users clicked through a 10%
of Firefox’s malware and phishing warnings, a 25% of Chrome’s malware
and phishing warnings, a 33% of Firefox’s SSL warnings, and 70% of
Google Chrome’s SSL warnings.

One area where I disagree with the authors is their belief that the
clickthrough rate for SSL warnings should be close to zero. While the
authors acknowledge the presence of false positives, they believe that
they should be close to zero and thus users should never click through
warnings. This can then incentivize developers to correct the security
problems users are encountering. While I agree with this goal, in
reality there will be sites that have not fixed security problems but
for which users still want to read their content. In these cases,
users may choose to click through an SSL warning but modify their
behavior to just read content and not login or submit other sensitive
information. Thus in practice, a clickthrough rate close to zero may
not be achievable.

I also believe the authors should have been more careful regarding
their conclusions. The authors make the following claim regarding the low
clickthrough rates in some cases:

    This demonstrates that security warnings can be effective in
    practice; security experts and system architects should not dismiss
    the goal of communicating security information to end users.

I do not think this follows from the study. They don't know whether
the *content* of the warnings has been heeded by the users, and
whether those warnings were understood. Because of the large-scale
nature of the study, they were not able to interview or survey users
regarding their knowledge or their choices. On the other hand, when
discussing somewhat higher clickthrough rates for Chrome SSL warnings,
the authors state that:

    This indicates that the user experience of a warning can have a
    significant impact on user behavior.

I strongly agree with this point, and the authors should have explored
this idea more fully. I don't believe the study shows that browsers
are doing a better job of communicating survey information to end
users.  But it has show that the user interface and user experience
can move users toward good security outcomes.

For example, regarding the results for malware and phishing warnings,
the clickthrough rates are higher for Chrome than for Firefox, even
though for Chrome you have to click twice and with Firefox you click
just once. One issue the authors don't mention is that in Chrome the
link to click through is prominently displayed next to the "Go Back"
button, whereas in Mozilla it is in smaller type and hidden on the
bottom right. Interface designs like this could help explain this
difference in behavior.

Likewise, for SSL warnings the clickthrough rates are higher for
Chrome than for Firefox. The authors fail to point out that the Google
design makes it exceptionally easy to click through, and has that
button appear first, with no appearance difference compared to leaving
the site. Firefox, on the other hand, has a fairly complex process to
enter an exception. Again, interface design could help explain the
difference in behavior.

Thus, it's not so much that people are learning more from warnings, or
paying more attention to them, but that the interface in Firefox has
discouraged people more strongly.

This points to the need for more work in this area. In a large-scale
study such as this, it is difficult to understand what users
understand, why they choose to ignore a security warning, and whether
they make "good" choices. To get at these issues, a follow-on work
could ask users to take a short survey when they click through a
security warning. This could be supplemented by network traces of user
activity showing what sites they visited and examining whether the
site posed a threat to the user.

References
==========

.. [1] Devdatta Akhawe and Adrienne Porter Felt. 2013. Alice in
       warningland: a large-scale field study of browser security
       warning effectiveness. In Proceedings of the 22nd USENIX
       conference on Security (SEC'13). USENIX Association, Berkeley,
       CA, USA, 257-272.
       http://dl.acm.org/citation.cfm?id=2534766.2534789
