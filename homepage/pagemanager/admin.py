# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):
	# Detail display

	# Automatically fill the url field based on what's given as title.
	prepopulated_fields = {'url': ('title',)}

	fieldsets = [
		(None,					{'fields': ['title']}),
		(_('Further options'),		{'fields': ['url', 'comment'], 'classes': ['collapse']}),
		(None,					{'fields': ['text']}),
	]
	
	# List display
	
	list_display = ('title', 'url')
	# Fields in which should be searched.
	search_fields = ['title', 'url', 'text']

admin.site.register(Page, PageAdmin)
