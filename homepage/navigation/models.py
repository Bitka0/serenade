# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.db import models

class Entry(models.Model):
	
	menuChoices = (
		("main", _('Main Menu')),
		("footer", _('Footer Menu')),
		("top", _('Top Menu')))
	
	name = models.CharField(_('name'), max_length=200, help_text = _('This name will be shown in the navigation.'))
	target = models.CharField(_('target'), max_length=200, help_text = _('Where the entry should point to.'))
	menu = models.CharField(_('menu'), max_length=200, choices=menuChoices, help_text = _('To which menu the entry will be assigned'))
	position = models.SmallIntegerField(_('position'), help_text = _('An integer, describing the position of this entry in the Navigation. Smaller numbers come first.'))
	
	class Meta:
		verbose_name = _('navigation entry')
		verbose_name_plural = _('navigation entries')
		ordering = ['position']
