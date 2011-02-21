# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
import django.template
from django.core.mail import send_mail
from settings import DEBUG, EMAIL_PREFIX, EMAIL_SENDER
import random
import base64
import hashlib

def generateSalt(length = 5):
	nbits = length * 6 + 1
	bits = random.getrandbits(nbits)
	uc = u"%0x" % bits
	newlen = int(len(uc) / 2) * 2 # we have to make the string an even length
	ba = bytearray.fromhex(uc[:newlen])
	return base64.urlsafe_b64encode(str(ba))[:length]

def pwEncode(password, salt):
	pwLength = len(password)
	if pwLength < 2:
		return hashlib.sha256(salt + password).hexdigest()

	firstChunk = password[:pwLength/2]
	secondChunk = password[pwLength/2:]

	return hashlib.sha256(salt + firstChunk + salt + secondChunk).hexdigest()

def stripSlash(string):
	if string[-1:] != '/':
		return string
	return string[:-1]

def generateContext(request, contextType = 'Context', **kwargs):
	if contextType.lower() == 'requestcontext':
		context = getattr(django.template, contextType)(request, kwargs)
	else:
		context = getattr(django.template, contextType)(kwargs)
	try:
		context['infoMessage'] = request.session['nextInfo']
		request.session['nextInfo'] = None
	except KeyError:
		pass

	return context

def doubleRange(a, b, **kwargs):
	d = tuple()
	for i in range(a, b, **kwargs):
		d += ((i,i),)
	return d

def sendMail(to, subject, message):
	send_mail('{0} {1}'.format(EMAIL_PREFIX, subject), message, EMAIL_SENDER, to, fail_silently = (DEBUG == False))
