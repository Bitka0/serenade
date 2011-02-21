# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.db import models
from django.contrib.auth.models import User
from django import forms


class Group(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	name=models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name

class Comment(models.Model):
	sender = models.CharField(max_length=80)
	date = models.DateTimeField(auto_now=True)
	homepage = models.CharField(max_length=200)
	
	subject = models.CharField(max_length=100)
	comment = models.TextField()

class CommentForm(forms.Form):
	subject = forms.CharField(max_length=100)
	message = forms.CharField()
	sender = forms.CharField(max_length=100)
	homepage = forms.CharField(max_length=200)
	
class Blogentry(models.Model):
	url = models.SlugField('URL', max_length=200, help_text = 'This field is automatically filled based on the title you enter, however if you want to customize the URL, here you can.')

	created_by = models.ForeignKey(User)
	publishingDate = models.DateTimeField(auto_now_add=True)
	lastModified = models.DateTimeField(auto_now=True)
	group = models.ManyToManyField(Group)
	tag = models.ManyToManyField(Tag)

	title = models.CharField(max_length=200)
	text = models.TextField()
	
	comment = models.ManyToManyField(Comment)
	
	def __unicode__(self):
		return self.title
