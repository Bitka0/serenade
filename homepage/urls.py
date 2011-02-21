# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Admin interface
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	
	# Catch-all for pagemanager, intentionally last.
	(r'^(?P<url>.*)$', 'pagemanager.views.show'),
)
