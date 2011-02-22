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
from django import forms
import util

def listAll(request):
	entrylist = Entry.objects.all().order_by('-publishingDate')
	context = util.generateContext(request, title = _('Blog'), entries = entrylist)
	return render_to_response('blog/standard.html', context)

def show(request, url):
	url = util.stripSlash(url)
	entry = get_object_or_404(Entry, url = url)
		
	if request.method == 'POST':
		form = CommentForm(request.POST)
		
		if form.is_valid():
			comment = Comment(entry = entry)
			comment.subject = form.cleaned_data['subject']
			comment.message = form.cleaned_data['message']
			comment.sender = form.cleaned_data['sender']
			comment.homepage = form.cleaned_data['homepage']
			comment.save()	
	else:
		form = CommentForm()
		
	context = util.generateContext(request, contextType = 'RequestContext', title = entry.title, entry = entry, commentform = form, comments = Comment.objects.filter(entry = entry).order_by('-date'))
	return render_to_response('blog/show.html', context)


def listGroups(request, url):
	url = util.stripSlash(url)
	entrylist = get_list_or_404(Entry, group__name = url)
	title = "Blog: " + url
	context = util.generateContext(request, title = title, entries = entrylist)
	return render_to_response('blog/standard.html', context)

def listTags(request, url):
	url = util.stripSlash(url)
	entrylist = get_list_or_404(Entry, tag__name = url)
	title = "Blog: " + url
	context = util.generateContext(request, title = title, entries = entrylist)
	return render_to_response('blog/standard.html', context)
