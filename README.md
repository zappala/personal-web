# Personal web pages

These are the web pages I use at my BYU home page,
http://zappala.byu.edu.

The pages are built using:

- [Pelican](http://docs.getpelican.com/en/3.3.0/)
- [Pelican Clear](https://github.com/zappala/pelican-clear)
- [Fabric](http://docs.fabfile.org/en/1.8/)

## Setup

First, create a virtual environment for pelican:

> sudo pip install virtualenv
> virtualenv ~/virtualenv/pelican

Then, install the required packages:

> pip install -r requirements.txt

## Use

Use

> fabric build

to build the web pages. Alternatively, use

> fab regenerate

to automatically regenerate the pages when they are changed. To
serve the pages, use

> fab serve

To publish, use

> fab publish

Copyright
---------

Copyright (c) 2013 Daniel Zappala

Released under the <a
href="http://creativecommons.org/licenses/by-sa/3.0/deed.en_US">Creative
Commons Attribution-ShareAlike 3.0 Unported License</a>.

