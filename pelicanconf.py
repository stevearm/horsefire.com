#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from   __future__ import unicode_literals
import os

AUTHOR = u'Steve Armstrong'
SITENAME = u'horsefire'
SITEURL = 'http://horsefire.com'
SITESUBTITLE = 'Put it out. PUT IT OUT!'
TIMEZONE = 'America/Los_Angeles'
DEFAULT_LANG = u'en'

# What directory is the content in?
PATH = 'content'

# Files/folders in PATH that will be copied instead of parsed
STATIC_PATHS = ['images', 'extra']

INDEX_SAVE_AS = 'blog/index.html'
ARTICLE_URL = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/'
ARTICLE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'
MONTH_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/{date:%m}/index.html'
YEAR_ARCHIVE_SAVE_AS = 'blog/{date:%Y}/index.html'
TAGS_SAVE_AS = 'blog/tags/index.html'
TAG_URL = 'blog/tags/{slug}'
TAG_SAVE_AS = 'blog/tags/{slug}/index.html'

AUTHORS_SAVE_AS = ''

# Setup theme
THEME = 'themes/main'

# Move files from their default location
# Using os.path.join() since the path must be os-specific (and I use Windows & Linux)
# Perhaps offer pull request against https://github.com/getpelican/pelican/issues/1133
# with an option to treat paths as os-agnostic
EXTRA_PATH_METADATA = {
    os.path.join('extra', 'robots.txt'): {'path': 'robots.txt'},
    os.path.join('extra', 'favicon.ico'): {'path': 'favicon.ico'}
}

# Add plugin
PLUGIN_PATH = 'plugins'
PLUGINS = ['main', ]

# Development-specific settings (these must be overridden for publishing)

RELATIVE_URLS = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
