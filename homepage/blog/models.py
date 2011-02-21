# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User

class Group(models.Model):
	name = models.CharField(_('name'), max_length=200)
	
	def __unicode__(self):
		return self.name
		
	class Meta:
		verbose_name = _('group')
		verbose_name_plural = _('groups')

class Tag(models.Model):
	name = models.CharField(_('name'), max_length=200)
	
	def __unicode__(self):
		return self.name

	class Meta:
		verbose_name = _('tag')
		verbose_name_plural = _('tags')

class Blogentry(models.Model):
	url = models.SlugField(_('URL'), max_length=200, help_text = _('This field is automatically filled based on the title you enter, however if you want to customize the URL, here you can.'))

	created_by = models.ForeignKey(User)
	publishingDate = models.DateTimeField(_('publication date'), auto_now_add=True)
	lastModified = models.DateTimeField(_('date of last modification'), auto_now=True)
	group = models.ManyToManyField(Group)
	tag = models.ManyToManyField(Tag)

	title = models.CharField(_('title'), max_length=200)
	text = models.TextField(_('text'))
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = _('blogentry')
		verbose_name_plural = _('blogentries')

