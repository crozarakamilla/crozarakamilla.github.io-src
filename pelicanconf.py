#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Kamilla Crozara'
SITENAME = 'Kamilla Crozara'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'America/Sao_Paulo'

DEFAULT_LANG = 'pt'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
THEME = '../voce/'
# short date format, optional but recommended
DEFAULT_DATE_FORMAT = "%b %d, %Y"
# change URL to point to desired logo for site
USER_LOGO_URL = "http://i.imgur.com/zzCRZUH.jpg"
TAGS_URL = 'tags.html'
ARCHIVES_URL = 'archives.html'

# Sample Links and Social Widget
LINKS = (('Home', '/index.html'),
         ('About', '/pages/about-me.html'),)

SOCIAL = (('Feed', '/feeds/all.atom.xml'),
          ('Email', 'mailto:xxx@gmail.com'),
          ('GitHub', 'http://github.com/limbenjamin'),)
