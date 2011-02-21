# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.template import Context, loader
from models import Redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
import util

def redirect(request, url):
	redirect = get_object_or_404(Redirect, url=url)
	return HttpResponseRedirect(redirect.target)
