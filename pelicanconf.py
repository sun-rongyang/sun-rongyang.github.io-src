#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Sun Rongyang'
SITENAME = "Sun Rongyang's Blog"
SITETITLE = AUTHOR
SITELOGO = "/images/avatar.jpg"
SITEURL = "http://localhost:8000"
BROWSER_COLOR = '#333333'
PYGMENTS_STYLE = 'monokai'
PYGMENTS_STYLE = 'solarized-dark'

PATH = 'content'
ARTICLE_PATHS = ['article']
ARTICLE_SAVE_AS = '{date:%Y}/{slug}.html'
ARTICLE_URL = '{date:%Y}/{slug}.html'
STATIC_PATHS = ["images", "article"]

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = 'en'

# Theme
THEME = "themes/Flex"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
# Blogroll
# LINKS = ((),)

# Social widget
SOCIAL = (("envelope-o", "mailto:sun-rongyang@outlook.com"),
          ("github", "https://github.com/sun-rongyang"),
          )

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

## Content
# Content cache
LOAD_CONTENT_CACHE = False
COPYRIGHT_NAME = "Sun Rongyang"
COPYRIGHT_YEAR = 2018
