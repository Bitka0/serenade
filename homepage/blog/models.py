# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.db import models

class Group(models.Model):
	name = models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name

class Tag(models.Model):
	name=models.CharField(max_length=200)
	
	def __unicode__(self):
		return self.name

class Blogentry(models.Model):
	url = models.SlugField('URL', max_length=200, help_text = 'This field is automatically filled based on the title you enter, however if you want to customize the URL, here you can.')

	publishingDate = models.DateTimeField(auto_now_add=True)
	lastModified = models.DateTimeField(auto_now=True)
	group = models.ManyToManyField(Group)
	tag = models.ManyToManyField(Tag)

	title = models.CharField(max_length=200)
	text = models.TextField()
	
	def __unicode__(self):
		return self.title


