# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.conf.urls.defaults import *
from feed.feeds import blogAll

# Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Admin interface
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/', include(admin.site.urls)),
	
	(r'^blog/$', 'blog.views.listAll'),
	(r'^blog/group/(?P<url>.*)$', 'blog.views.listGroups'),
	(r'^blog/tag/(?P<url>.*)$', 'blog.views.listTags'),
	(r'^blog/(?P<url>.*)$', 'blog.views.show'),
	(r'^blog/feed/$', blogAll()),
)
