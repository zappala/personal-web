Personal web pages
==================

These are the web pages I use at my BYU home page,
http://zappala.byu.edu.

The pages are built using:

- [Flask](http://flask.pocoo.org/)
- [Frozen-Flask](http://pythonhosted.org/Frozen-Flask/)
- [Twitter Bootstrap](http://twitter.github.io/bootstrap/)
- [DoIt](http://pydoit.org/)

Use

> python app.py

to start a local server with the web pages, and

> python app.py build

to build a static set of pages you can place on any web server. To
deploy, edit dodo.py and use

> doit

to rsync the pages to a remote server.

Copyright
---------

Copyright (c) 2013 Daniel Zappala

Released under the <a
href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative
Commons Attribution-ShareAlike 3.0 Unported License</a>.

