# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.template import Context, loader
from models import Entry, Group, Tag
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
from search.models import Searchform
from django import forms
from django.core.paginator import Paginator, InvalidPage, EmptyPage
import util

def listAll(request, page=None):
	try:
		page = int(util.stripSlash(page))
	except:
		page = 1
	entrylist = Entry.objects.all().filter(published = True)
	paginator = Paginator(entrylist, 15)
	try:
		entrylist = paginator.page(page)
	except (EmptyPage, InvalidPage):
		return redirect("/blog/")
	
	uri = util.getUri(request)
	context = util.generateContext(request, contextType = 'RequestContext', entries = entrylist, fulluri = uri)
	return render_to_response('blog/standard.html', context)

def show(request, url):
	url = util.stripSlash(url)
	entry = get_object_or_404(Entry, url = url, published = True)
	searchform = Searchform()
	context = util.generateContext(request, contextType = 'RequestContext', title = entry.title, entry = entry, searchform = searchform, url = url)
	return render_to_response('blog/show.html', context)


def listGroups(request, url):
	url = util.stripSlash(url)
	try:
		url, page = url.split("/")
	except:
		page = 1
	entrylist = get_list_or_404(Entry, groups__name = url, published = True)
	paginator = Paginator(entrylist, 15)
	entrylist = paginator.page(page)
	title = "Blog: " + url
	uri = util.getUri(request)
	context = util.generateContext(request, title = title, entries = entrylist, fulluri = uri)
	return render_to_response('blog/standard.html', context)

def listTags(request, url, page=None):
	try:
		url = int(util.stripSlash(url))
	except:
		url = 1

	entrylist = get_list_or_404(Entry, tags__name = url, published = True)
	paginator = Paginator(entrylist, 15)
	entrylist = paginator.page(page)
	title = "Blog: " + url
	uri = util.getUri(request)
	context = util.generateContext(request, title = title, entries = entrylist, fulluri = uri)
	return render_to_response('blog/standard.html', context)
