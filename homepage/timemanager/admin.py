# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
	def save_model(self, request, obj, form, change):
		if obj.startTime == None:
			obj.startTime = '00:00:00'
		if obj.endTime == None:
			obj.endTime = '23:59:00'
		if obj.startTime == '00:00:00' and obj.endTime == '23:59:00':
			obj.wholeDay = True
		else:
			obj.wholeDay = False
		obj.save()

	
	fieldsets = [
		(None,						{'fields': ['name', 'published']}),
		(None,						{'fields': ['description']}),
		(_('Date'),					{'fields': [('startDay', 'endDay'), ('startTime', 'endTime')]}),
		(_('Further options'),		{'fields': ['url']}),
	]
	
	# Automatically fill the url field based on what's given as title.
	prepopulated_fields = {'url': ('name',)}
	
	search_fields = ['name', 'url', 'description']
	
	list_display = ('name', 'wholeDay', 'startDay', 'endDay', 'startTime', 'endTime', 'published')
	list_filter = ('published',)

admin.site.register(Entry, EntryAdmin)
