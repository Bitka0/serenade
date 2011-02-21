# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from models import Blogentry, Group, Tag
from django.contrib import admin

class BlogAdmin(admin.ModelAdmin):#
	# Detail display

	# Automatically fill the url field based on what's given as title.
	prepopulated_fields = {'url': ('title',)}

	
	# List display
	
	list_display = ('title', 'url')
	# Fields in which should be searched.
	search_fields = ['title', 'url', 'text']

class Groupadmin(admin.ModelAdmin):
	list_display= ('name',)

class Tagadmin(admin.ModelAdmin):
	list_display= ('name',)

admin.site.register(Blogentry, BlogAdmin)
admin.site.register(Group, Groupadmin)
admin.site.register(Tag, Tagadmin)
