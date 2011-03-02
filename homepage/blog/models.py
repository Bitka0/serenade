# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.db import models
from django.contrib.auth.models import User
from django import forms


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

class Entry(models.Model):
	url = models.SlugField(_('URL'), max_length=200, help_text = _('This field is automatically filled based on the title you enter, however if you want to customize the URL, here you can.'))

	author = models.ForeignKey(User, verbose_name = _('author'))
	creationDate = models.DateTimeField(_('publication date'), auto_now_add=True)
	published = models.BooleanField(_('published'))
	lastModified = models.DateTimeField(_('date of last modification'), auto_now=True)
	groups = models.ManyToManyField(Group, verbose_name = _('groups'), blank=True)
	tags = models.ManyToManyField(Tag, verbose_name = _('tags'), blank=True)

	title = models.CharField(_('title'), max_length=200)
	text = models.TextField(_('text'))
	admincomment = models.TextField(_('comment'), help_text = _('What you enter here is only displayed in the admin area.'), blank=True)
	
	enable_comments = models.BooleanField(_('enable comments'), default=True)
	
	def __unicode__(self):
		return self.title
	
	def get_absolute_url(self):
		return '/blog/{0}/'.format(self.url)
	get_absolute_url.short_description = _('absolute URL')
	get_absolute_url.admin_order_field = 'url'

	def getLink(self):
		return '<a href="{0}">{1}</a>'.format(self.get_absolute_url(), self.url)
	getLink.allow_tags = True
	getLink.short_description = _('URL')
	getLink.admin_order_field = 'url'

	class Meta:
		verbose_name = _('blogentry')
		verbose_name_plural = _('blogentries')
		ordering = ['-creationDate']
