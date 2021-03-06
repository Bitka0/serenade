# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.conf.urls.defaults import *
from feed.feeds import blogAll, selectGroup, selectTag
from feed.sitemap import MainSitemap

# Admin
from django.contrib import admin
admin.autodiscover()

sitemaps = {
    'main': MainSitemap,
}

urlpatterns = patterns('',
	# Admin interface
	(r'^admin/filebrowser/', include('filebrowser.urls')),
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/', include(admin.site.urls)),
	
	(r'^blog/(?P<page>\d*)$', 'blog.views.listAll'),
	(r'^blog/group/feed/(?P<url>.*)$', selectGroup()),
	(r'^blog/group/(?P<url>.*)$', 'blog.views.listGroups'),
	(r'^blog/group/(?P<url>.*)/(?P<page>\d*)$', 'blog.views.listGroups'),
	(r'^blog/tag/feed/(?P<url>.*)$', selectTag()),
	(r'^blog/tag/(?P<url>.*)$', 'blog.views.listTags'),
	(r'^blog/tag/(?P<url>.*)/(?P<page>\d*)$', 'blog.views.listTags'),
	(r'^blog/feed/$', blogAll()),
	(r'^blog/(?P<url>.*)$', 'blog.views.show'),
	
	(r'^calendar/show/(?P<url>.*)$', 'timemanager.views.showEvent'),
	(r'^calendar/(?P<url>.*)$', 'timemanager.views.showCalendar'),
	
	(r'^search/$', 'search.views.searchAll'),
	
	(r'^comments/', include('django.contrib.comments.urls')),
	
	(r'^user/login/$', 'usermanag.views.userlogin'),
	(r'^user/showlogin/$', 'usermanag.views.showlogin'),
	(r'^user/logout/$', 'usermanag.views.userlogout'),
	
	(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.sitemap', {'sitemaps': sitemaps}),
	
	(r'^ping/', include('trackback.urls')),

)
