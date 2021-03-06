#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os
import sys

# Basic Settings
AUTHOR = u'Akshay Pratap Singh'
SITENAME = u'#kodekracker'
SITEURL = 'http://localhost:8080'

# path to content directory
PATH = 'content'

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{date:%d}/{slug}/index.html'

DRAFT_URL = 'drafts/{slug}'
DRAFT_SAVE_AS = 'drafts/{slug}.html'

PAGE_URL = 'pages/{slug}'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

CATEGORY_URL = 'category/{slug}'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = 'tag/{slug}/index.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'

ARCHIVES_SAVE_AS = 'archives.html'

# set theme
THEME = "theme/pelican-bootstrap3"

# set timezone
TIMEZONE = 'Asia/Kolkata'

# set defualt language format
DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

try:
    PLUGIN_PATHS = [os.environ["PELICAN_PLUGINS_PATH"]]
except KeyError:
   print "==> Please set the environment variable PELICAN_PLUGINS_PATH"
   sys.exit(1)

PLUGINS = ['gravatar', 'tipue_search', 'i18n_subsites']
STATIC_PATHS = ['images','static','extra']

EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'}
}

PAGE_ORDER_BY = 'sortorder'
SITESUBTITLE = "aksjdsjdsfsd"

JINJA_ENVIRONMENT = {
    'extensions': ['jinja2.ext.i18n'],
}


## Pelican Bootstrap 3 Theme
## Template Settings

# show pages menu on topbar
DISPLAY_PAGES_ON_MENU = True

# show category menu on topbar
DISPLAY_CATEGORIES_ON_MENU = False

# add menu on top bar Ex:- MENUITEMS = [('XYZ','http://xyz.com')]
MENUITEMS = []

DROPDOWNITEMS = [('Tumblr Blog', 'http://tumblr.akshayon.net'),
            ('Movies Listing','http://movies.akshayon.net')]

# set bootswatch theme
# Bootswatch(http://bootswatch.com/), Free themes for Bootstrap
BOOTSTRAP_THEME = "flatly"

# show the author of the article at the top of the article
SHOW_ARTICLE_AUTHOR = False

# show the Category of each article
SHOW_ARTICLE_CATEGORY = True

# show the article modified date next to the published date
SHOW_DATE_MODIFIED = True

# add custom css to the theme Ex:- CUSTOM_CSS = 'static/custom.css'
CUSTOM_CSS = 'static/css/custom.css'

# code syntax highlighting style
PYGMENTS_STYLE = "tango"

# use Boostrap3 Pager
USE_PAGER = True

# use the fluid container layout from Bootstrap
BOOTSTRAP_FLUID = False

# set logo for your site Ex:- SITELOGO = 'images/my_site_logo.png'
# SITELOGO = ''

# set logo height and width will be set accordingly
# SITELOGO_SIZE =

# hide the site name
HIDE_SITENAME = False

# show breadcrumbs in site
DISPLAY_BREADCRUMBS = True

# show article category in the breadcrumbs
DISPLAY_CATEGORY_IN_BREADCRUMBS = False

# use the inverse navbar from Bootstrap
BOOTSTRAP_NAVBAR_INVERSE = True

## Related Plugin Config
# limit related post
RELATED_POSTS_MAX = 3

# show related posts from categories other than the original article's
RELATED_POSTS_SKIP_SAME_CATEGORY = False

## Series Plugin Config
# display on the sidebar the link to the previous and next article
# in the series
DISPLAY_SERIES_ON_SIDEBAR = False

# display information on the series just under the article title
SHOW_SERIES = False

# set favicon
FAVICON = 'images/favicon.ico'

# article info (date, tags) will be show under the title for each article
DISPLAY_ARTICLE_INFO_ON_INDEX = True

# show about text on side bar
ABOUT_ME = 'Software Developer and Data Science Enthusiast'

# show avatar on side bar
AVATAR = "images/profile.jpeg"

# Set the banner image Ex:- BANNER = '/path/to/banner.png'
# BANNER = '/path/to/banner.png'

# Set the subtitle text Ex:- BANNER_SUBTITLE = 'This is my subtitle'
# BANNER_SUBTITLE = 'This is my subtitle'

# display the banner on all pages
# BANNER_ALL_PAGES = True

# Social widget
SOCIAL = (('Facebook', 'https://www.facebook.com/spratapakshay'),
          ('Twitter', 'https://twitter.com/spratapakshay'),
          ('Google+','https://plus.google.com/+AkshayPratap_01'),
          ('Linkedin','https://in.linkedin.com/in/spratapakshay'),
          ('Github','https://github.com/KodeKracker/'),
          ('LastFm', 'http://www.last.fm/user/AKSHAYPRATAP007'),
          ('Stack-Overflow', 'https://careers.stackoverflow.com/kodekracker'))

# show tags on sidebar
DISPLAY_TAGS_ON_SIDEBAR = False

# display the tags inline
DISPLAY_TAGS_INLINE = True

# show category on sidebar
DISPLAY_CATEGORIES_ON_SIDEBAR = True

# show recent post on sidebar
# DISPLAY_RECENT_POSTS_ON_SIDEBAR = True

# control the amount of recent posts
# RECENT_POST_COUNT = 5

# to remove sidebar entirely
HIDE_SIDEBAR = False

## Disqus Config
# sets identifiers for each article's comment threads
#  DISQUS_NO_ID = True

# set slug as prefix in id
DISQUS_ID_PREFIX_SLUG = True

# show Disqus comment counts on the index page
DISQUS_DISPLAY_COUNTS = True

# choose the license by name
# "CC-BY" (require attribution)
# "CC-BY-SA" (require ShareAlike)
# "CC-BY-ND" (NoDerivatives)
# "CC-BY-NC" (require attribution, no commercial reuse)
# "CC-BY-NC-SA" (require ShareAlike, no commercial reuse)
# "CC-BY-NC-ND" (NoDerivatives, no commercial reuse).
CC_LICENSE = "CC-BY-NC-SA"

# choose the licence by features
# CC_LICENSE_DERIVATIVES = "yes"
# CC_LICENSE_COMMERCIAL = "yes"

# include attribution markup in the license mark
CC_ATTR_MARKUP = True

# set custom license
# CUSTOM_LICENSE='Unless otherwise stated, all articles are published under the <a href="http://www.wtfpl.net/about/">WTFPL</a> license.'

# show your most recently active GitHub repos in the sidebar
# GITHUB_USER = 'username'
# GITHUB_REPO_COUNT =
# GITHUB_SKIP_FORK =
# GITHUB_SHOW_USER_LINK =

# disable Facebook Open Graph
USE_OPEN_GRAPH = True

# set Facebook Open Graph App ID
# OPEN_GRAPH_FB_APP_ID = ''

# set a default image as an Open Graph tag
# OPEN_GRAPH_IMAGE = ''

# enable Twitter Summary Card
TWITTER_CARDS = True
USE_OPEN_GRAPH = True

# set Twitter Account Username
TWITTER_USERNAME = 'spratapakshay'

# set Twitter Widget ID for Twitter Timeline
TWITTER_WIDGET_ID = os.getenv('TWITTER_WIDGET_ID',None)

# limit the tweets count
TWEET_LIMIT = 3

# enable Shariff Sharing Content
SHARIFF = True

# SHARIFF_BACKEND_URL = 'url'
SHARIFF_LANG = 'en' # 'de', 'fr'
# SHARIFF_ORIENTATION = 'horizontal' or 'vertical'
# SHARIFF_SERVICES = [&quot;facebook&quot;,&quot;googleplus&quot;]
# SHARIFF_THEME = 'standard' or 'grey'
SHARIFF_TWITTER_VIA = True # False

# for Tipue Search
DIRECT_TEMPLATES = ('index', 'categories', 'authors', 'archives', 'search')
