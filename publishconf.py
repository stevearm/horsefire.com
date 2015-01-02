#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

FEED_DOMAIN = SITEURL

FEED_RSS = 'blog/feed/index.xml'
FEED_ATOM = 'blog/feed/atom/index.xml'

FEED_MAX_ITEMS = 50

DELETE_OUTPUT_DIRECTORY = True
RELATIVE_URLS = False

GOOGLE_ANALYTICS = 'UA-33722666-1'
DISQUS_SITENAME = 'horsefire'
