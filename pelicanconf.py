#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# Basic site info
AUTHOR = u'Daniel Zappala'
TAGLINE = u'Associate Professor'
AFFILIATION = u'<a href="https://byu.edu">BYU</a> | <a href="https://cs.byu.edu">Computer Science</a>'
SITENAME = u'Daniel Zappala'
SITEURL = 'https://zappala.byu.edu'

# Contact info
EMAIL = 'daniel.zappala@gmail.com'
GITHUB_URL = 'https://github.com/zappala'
GOOGLEPLUS_URL = 'https://plus.google.com/114449822521576560110?prsrc=3'
TWITTER_URL = 'https://twitter.com/Daniel_Zappala'
LINKEDIN_URL = 'https://www.linkedin.com/in/danielzappala/'

ADDRESS = '3361 TMCB, Brigham Young University, Provo, UT 84062'
PHONE = '801-422-2195'

# Customization
LINKS_LABEL = 'Director:'
LINKS = [('Internet Research Lab','https://internet.byu.edu'),
         ('BYU Open Source Lab','https://osl.byu.edu')]

LICENSE = '<a rel="license" href="https://creativecommons.org/licenses/by-sa/3.0/deed.en_US"><img alt="Creative Commons License" style="border-width:0" src="https://i.creativecommons.org/l/by-sa/3.0/88x31.png" /></a>'
COPYRIGHT = '2013 Daniel Zappala'

TIMEZONE = 'US/Mountain'
DEFAULT_LANG = u'en'

# How to save pages
PAGE_URL = '{slug}'
PAGE_SAVE_AS = '{slug}/index.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%b}/{date:%d}/{slug}/index.html'
INDEX_SAVE_AS = 'blog/index.html'

# Templates
DIRECT_TEMPLATES = ('index', 'tags', 'archives')

# Feeds
FEED_DOMAIN = SITEURL
TAG_FEED_ATOM = 'feeds/tag-%s.atom.xml'

# Misc
ARTICLE_PATHS = ['blog']
STATIC_PATHS = ['images','docs','lib','pubs','talks','summaries']
DEFAULT_PAGINATION = 10

# Theme
USER_LOGO_URL = "/images/daniel-zappala.jpg"
THEME = "themes/pelican-clear"

# Plugins
PLUGIN_PATHS = ['plugins']
PLUGINS = ['neighbors']

# Comments
DISQUS_SITENAME	= 'zappala'

# For development only
RELATIVE_URLS = True
