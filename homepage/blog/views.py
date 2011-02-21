# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.template import Context, loader
from models import Blogentry, Group, Tag
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.core.urlresolvers import reverse
from django import forms
import util

def listAll(request):

	entrylist = Blogentry.objects.all().order_by('-publishingDate')
	context = util.generateContext(request, entries = entrylist)
	return render_to_response('blog/standard.html', context)

def show(request, url):
	url = util.stripSlash(url)

	if url == '' or url == None:
		url = '/'

	entry = get_object_or_404(Blogentry, url=url)
	context = util.generateContext(request, title = entry.title, text = entry.text, groups = entry.group.all(), tags = entry.tag.all(), pubDate = entry.publishingDate, created_by = entry.created_by)
	return render_to_response('blog/show.html', context)
