# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from models import Page
from django.contrib import admin

class PageAdmin(admin.ModelAdmin):#
	# Automatically fill the url field based on what's given as title.
	prepopulated_fields = {'url': ('title',)}

	fieldsets = [
		(None,					{'fields': ['title']}),
		('Further options',		{'fields': ['url', 'comment'], 'classes': ['collapse']}),
		(None,					{'fields': ['text']}),
	]

admin.site.register(Page, PageAdmin)
