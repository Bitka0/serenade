# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

# –––––––––––––––––––––
# General Settings
# –––––––––––––––––––––

# Do we run in production mode?
PRODUCTION = False

# Enter your name and email here. You can define multiple admins.
ADMINS = (
	('Lazy Admin', 'lazy@admin.org'),
)

# Choose whatever you want.
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'

# Make this one unique
SECRET_KEY = 'this-is-not-unique'

# –––––––––––––––––––––
# Email Settings
# –––––––––––––––––––––

EMAIL_PREFIX = '[Serenade]'
EMAIL_SENDER = 'lazy@admin.org'


# –––––––––––––––––––––
# Database settings
# –––––––––––––––––––––

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
		'NAME': 'database.db',                      # Or path to database file if using sqlite3.
		'USER': '',                      # Not used with sqlite3.
		'PASSWORD': '',                  # Not used with sqlite3.
		'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
		'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
	}
}

# –––––––––––––––––––––
# Caching
# –––––––––––––––––––––

# Uncomment if you want caching.
#CACHES = {
#	'default': {
#		'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#		'LOCATION': '127.0.0.1:11211',
#	}
#}




# DO NOT EDIT AFTER THIS LINE UNLESS YOU KNOW WHAT YOU'RE DOING (Most probably you don't).

import os

TEMPLATE_DEBUG = DEBUG = (PRODUCTION == False)

MANAGERS = ADMINS
SITE_ID = 1
USE_I18N = True
USE_L10N = True
GRAPPELLI_INDEX_DASHBOARD = 'homepage.dashboard.CustomIndexDashboard'
GRAPPELLI_ADMIN_TITLE = 'Serenade'
FORCE_SCRIPT_NAME = ''
STATIC_URL = '/assets/'
STATIC_ROOT = '{0}/../assets/'.format(os.getcwd())
MEDIA_ROOT = '{0}media/'.format(STATIC_ROOT)
MEDIA_URL = '{0}media/'.format(STATIC_URL)
FILEBROWSER_DIRECTORY = MEDIA_ROOT

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
	'django.middleware.common.CommonMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	
	# Intentionally last
	'django.contrib.redirects.middleware.RedirectFallbackMiddleware',
	'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
	# default template context processors
	'django.core.context_processors.auth',
	'django.core.context_processors.debug',
	'django.core.context_processors.i18n',
	'django.core.context_processors.media',

	# django 1.2 only
	'django.contrib.messages.context_processors.messages',

	# required by grappelli
	'django.core.context_processors.request',
)

ROOT_URLCONF = 'homepage.urls'

TEMPLATE_DIRS = (
	'{0}/../templates'.format(os.getcwd())
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.sites',
	'staticfiles',
	
	# Admin interface
	'grappelli.dashboard',
	'grappelli',
	'django.contrib.admin',
	'filebrowser',

	# Static pages
	'django.contrib.flatpages',
	# Redirects
	'django.contrib.redirects',

	'homepage.navigation',
	'homepage.blog',
)
