# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404, redirect
import util
from django.contrib.auth import authenticate, login, logout

def userlogin(request):
	username = request.POST['username']
	password = request.POST['password']
	user = authenticate(username=username, password=password)
	if user is not None:
		if user.is_active:
			login(request, user)
			title = _("Login was successful")
			message = _("Welcome {0}".format(username))
		else:
			title = _("Login failed")
			message = _("The account is disabled")
	else:
		title = _("Login failed")
		message = _("Username and/or password wrong")
	context = util.generateContext(request, contextType = 'RequestContext', title = title, message = message)
	return render_to_response('user/login.html', context)

def userlogout(request):
	logout(request)
	context = util.generateContext(request, contextType = 'RequestContext', title = _("Logout was successful"), message = _("You were successfully logged out"))
	return render_to_response('user/login.html', context)

def showlogin(request):
	context = util.generateContext(request, contextType = 'RequestContext', title = _("Login"))
	return render_to_response('user/login.html', context)
