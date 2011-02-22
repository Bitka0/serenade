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

	created_by = models.ForeignKey(User, verbose_name = _('creator'))
	publishingDate = models.DateTimeField(_('publication date'), auto_now_add=True)
	lastModified = models.DateTimeField(_('date of last modification'), auto_now=True)
	groups = models.ManyToManyField(Group, verbose_name = _('groups'), blank=True)
	tags = models.ManyToManyField(Tag, verbose_name = _('tags'), blank=True)

	title = models.CharField(_('title'), max_length=200)
	text = models.TextField(_('text'))
	admincomment = models.TextField(_('comment'), help_text = _('What you enter here is only displayed in the admin area.'))
	
	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = _('blogentry')
		verbose_name_plural = _('blogentries')

class Comment(models.Model):
	entry = models.ForeignKey(Entry, verbose_name = _('related blog entry'))
	sender = models.CharField(_('author'), max_length=80)
	date = models.DateTimeField(_('date of creation'), auto_now=True)
	homepage = models.CharField(_('homepage'), max_length=200, blank=True)
	
	subject = models.CharField(_('subject'), max_length=100, blank=True)
	message = models.TextField(_('comment'))

	class Meta:
		verbose_name = _('comment')
		verbose_name_plural = _('comments')

class CommentForm(forms.Form):
	subject = forms.CharField(max_length=100, required=False)
	message = forms.CharField()
	sender = forms.CharField(max_length=100)
	homepage = forms.CharField(max_length=200, required=False)
