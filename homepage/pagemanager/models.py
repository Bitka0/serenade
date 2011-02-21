# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.db import models

class Page(models.Model):
	url = models.SlugField(_('URL'), max_length=200, help_text = _('This field is automatically filled based on the title you enter, however if you want to customize the URL, here you can.'))

	title = models.CharField(_('title'), max_length=200)
	comment = models.TextField(_('comment'), help_text = _('Internal comment on the page, never displayed publicly.'), blank = True)
	text = models.TextField(_('text'))

	def __unicode__(self):
		return self.title

	class Meta:
		verbose_name = _('page')
		verbose_name_plural = _('pages')
