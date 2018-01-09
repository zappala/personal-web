The Cognitive Walkthrough Method: A Practitioner's Guide
########################################################

:date: 2016-01-19
:tags: usability, cognitive walkthrough, methods
:slug: the-cognitive-walkthrough-method-a-practitioners-guide
:author: Daniel Zappala

Paper review: `The Cognitive Walkthrough Method: A Practitioner's Guide <http://www.colorado.edu/ics/sites/default/files/attached-files/93-07.pdf>`__, by Cathleen Wharton, John Rieman, Clayton Lewis, and Peter Polson (University of Colorado), Technical Report #93-07 [1]_.

This paper describes the cognitive walkthrough method for evaluating the usability of software. With this method, the
developers of a system evaluate how well users can accomplish specific tasks.


This method is intended
to be used by the developers of a system to evaluate how well their interface is designed for users. It is practiced
by developers, without input from users of the system. The idea is to get feedback from peers regarding how well your
system enables users to accomplish a given task, early in the design stage (e.g. with paper designs). The system
can then be improved, and additional walkthroughs performed until the system is polished. At that point, the system is
ready for user testing.

This is a method used by developers of a system. It is not a measurement of real users.
It is advantageous because it is cheap (don't have to bring users into your lab, just schedule a meeting).
Its disadvantage is that the coverage may not be complete, or you may find things that are not a problem for actual users.
The idea is to iron out obvious problems before doing user testing. Revise and repeat until ready to test with users.



-- insights from doing our own walkthrough

- method does not allow the researchers to explore paths the users might take instead of the right path
- method requires you to follow steps past "severely broken UI" so this feels useless
- method assumes user knows the right task to start with
- boundary between question 2 and 3 is difficult to ascertain

- method could be useful for researchers as opposed to software developers if they are simply seeking to understand
  an existing product

- Three obvious broken things in Mailvelope
  - user doesn't know to setup their own keys or what they are for
  - user doesn't know to ask recipient for their key -- nor best way to get it
  - user doesn't know to click icon to send encrypted email
- Mailvelope assumes you've watched their tutorial so these actions are obvious?
