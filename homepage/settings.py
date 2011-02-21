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
ADMIN_MEDIA_PREFIX = '/media/'

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
)

ROOT_URLCONF = 'homepage.urls'

TEMPLATE_DIRS = (
	'{0}/../templates'.format(os.getcwd())
)

INSTALLED_APPS = (
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.sites',
	'django.contrib.messages',
	'django.contrib.admin',
	'django.contrib.admindocs',
)
