# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.template import Context, loader
from models import Entry, Group, Tag, Comment, CommentForm
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from search.models import Searchform
from django import forms
import util

def listAll(request, url=None):
	if url != None:
		url = int(util.stripSlash(url))
	else:
		url = 0
	entrylist = Entry.objects.all().filter(published = True)[url:15]
	context = util.generateContext(request, contextType = 'RequestContext', title = _('Blog'), entries = entrylist)
	return render_to_response('blog/standard.html', context)

def show(request, url):
	url = util.stripSlash(url)
	entry = get_object_or_404(Entry, url = url, published = True)
		
	if request.method == 'POST':
		form = CommentForm(request.POST)
		
		if form.is_valid():
			comment = Comment(entry = entry)
			comment.subject = form.cleaned_data['subject']
			comment.message = form.cleaned_data['message']
			comment.sender = form.cleaned_data['sender']
			comment.homepage = form.cleaned_data['homepage']
			comment.save()	
	
	form = CommentForm()
	searchform = Searchform()
	context = util.generateContext(request, contextType = 'RequestContext', title = entry.title, entry = entry, commentform = form, comments = Comment.objects.filter(entry = entry), searchform = searchform)
	return render_to_response('blog/show.html', context)


def listGroups(request, url):
	url = util.stripSlash(url)
	entrylist = get_list_or_404(Entry, groups__name = url, published = True)
	title = "Blog: " + url
	context = util.generateContext(request, title = title, entries = entrylist)
	return render_to_response('blog/standard.html', context)

def listTags(request, url):
	url = util.stripSlash(url)
	entrylist = get_list_or_404(Entry, tags__name = url, published = True)
	title = "Blog: " + url
	context = util.generateContext(request, title = title, entries = entrylist)
	return render_to_response('blog/standard.html', context)
