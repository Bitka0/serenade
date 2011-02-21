# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.template import Context, loader
from models import Blogentry, Group, Tag, Comment, CommentForm
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
		
	if request.method == 'POST':
		form = CommentForm(request.POST) # A form bound to the POST data
		if form.is_valid(): # All validation rules pass
			# Process the data in form.cleaned_data
			# ...
				return HttpResponseRedirect('/thanks/') # Redirect after POST
	else:
		form = CommentForm() # An unbound form
		
	entry = get_object_or_404(Blogentry, url=url)
	context = util.generateContext(request, title = entry.title, text = entry.text, url = entry.url, groups = entry.group.all(), tags = entry.tag.all(), pubDate = entry.publishingDate, created_by = entry.created_by, commentform = form, comments = entry.comment)
	return render_to_response('blog/show.html', context)

