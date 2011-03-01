# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.template import Context, loader
from models import Searchform
from blog import models
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django import forms
import util

def searchAll(request):
	if request.method == 'POST':
		form = Searchform(request.POST)
		
		if form.is_valid():
			searchstring = form.cleaned_data['searchbox']
			entrylist = models.Entry.objects.filter(title__search='Leitbild')
			context = util.generateContext(request, title = _('Search'), entries = entrylist)
			return render_to_response('search/result.html', context)
