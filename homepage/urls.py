# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.conf.urls.defaults import *
from redirector.models import Redirect
from pagemanager.models import Page
from django.shortcuts import get_object_or_404
import redirector.views
import pagemanager.views
import util

# Admin
from django.contrib import admin
admin.autodiscover()

# FIXME: Find a nicer solution for this.
def catchAll(request, url):
	url = util.stripSlash(url)
	try:
		redirect = Redirect.objects.get(url = url)
		return redirector.views.redirect(request, url)
	except:
		get_object_or_404(Page, url = url)
		return pagemanager.views.show(request, url)

urlpatterns = patterns('',
	# Admin interface
	(r'^grappelli/', include('grappelli.urls')),
	(r'^admin/doc/', include('django.contrib.admindocs.urls')),
	(r'^admin/', include(admin.site.urls)),
	
	(r'^blog/$', 'blog.views.listAll'),
	(r'^blog/(?P<url>.*)$', 'blog.views.show'),
	
	# Catch-all for redirector, intentionally last.
	#(r'^(?P<url>.*)$', 'redirector.views.redirect'),

	# Catch-all for pagemanager, intentionally last.
	(r'^(?P<url>.*)$', catchAll),
)
