# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.conf.urls.defaults import *
from feed.feeds import blogAll, selectGroup, selectTag

# Admin
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Admin interface
	(r'^admin/filebrowser/', include('filebrowser.urls')),
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/', include(admin.site.urls)),
	
	(r'^blog/(?P<url>\d{1})$', 'blog.views.listAll'),
	(r'^blog/(?P<url>\d*)$', 'blog.views.listAll'),
	(r'^blog/group/feed/(?P<url>.*)$', selectGroup()),
	(r'^blog/group/(?P<url>.*)$', 'blog.views.listGroups'),
	(r'^blog/tag/feed/(?P<url>.*)$', selectTag()),
	(r'^blog/tag/(?P<url>.*)$', 'blog.views.listTags'),
	(r'^blog/feed/$', blogAll()),
	(r'^blog/(?P<url>.*)$', 'blog.views.show'),
	
	(r'^calendar/show/(?P<url>.*)$', 'timemanager.views.showEvent'),
	(r'^calendar/(?P<url>.*)$', 'timemanager.views.showCalendar'),
	
	(r'^search/$', 'search.views.searchAll'),
	
	(r'^comments/', include('django.contrib.comments.urls')),
)
