# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.template import Context, loader
from models import Page
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django import forms
import util

def show(request, url):
	url = util.stripSlash(url)

	if url == '' or url == None:
		url = '/'

	page = get_object_or_404(Page, url=url)
	context = util.generateContext(request, title = page.title, text = page.text)
	return render_to_response('pagemanager/standard.html', context)
