# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.db import models

class Entry(models.Model):
	name = models.CharField(_('name'), max_length = 200)
	description = models.TextField(_('description'), blank = True)
	
	published = models.BooleanField(_('published'))
	
	# When
	startDay = models.DateField(_('start day'))
	endDay = models.DateField(_('end day'))
	
	startTime = models.TimeField(_('start time'), blank = True, help_text = _('If you omit this field, it is assumed this event takes part the whole day.'))
	endTime = models.TimeField(_('end time'), blank = True, help_text = _('If you omit this field, it is assumed this event takes part the whole day.'))
	
	def wholeDay(self):
		if not self.startTime or not self.endTime:
			return True
		return False
	
	wholeDay.short_description = _('Whole day')
	
	class Meta:
		verbose_name = _('Calendar entry')
		verbose_name_plural = _('Calendar entries')
