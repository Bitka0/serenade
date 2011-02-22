# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

try:
	from secretsettings import *
except ImportError:
	print("It seems like you've forgotten to create a secretsettings.py, don't you?")
	exit(1)

import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
	('Lukas Martini', 'lukas.martini@unionhost.de'),
	('Phillip Thelen', 'phillip.thelen@junge-piraten.de'),
)

MANAGERS = ADMINS
TIME_ZONE = 'Europe/Berlin'
LANGUAGE_CODE = 'de-de'
SITE_ID = 1
USE_I18N = True
USE_L10N = True
MEDIA_ROOT = ''
MEDIA_URL = ''

STATIC_URL = '/static/'
STATIC_ROOT = '{0}/../tmp/'.format(os.getcwd())

STATICFILES_DIRS = (
	'{0}/../static/'.format(os.getcwd()),
)

ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"

EMAIL_PREFIX = '[Junge Piraten]'
EMAIL_SENDER = 'it@junge-piraten.de'

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

	# required by django-admin-tools
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
	'grappelli',
	'django.contrib.admin',
	'django.contrib.admindocs',

	# Static pages
	'django.contrib.flatpages',

	'homepage.blog',
	'homepage.redirector'
)
