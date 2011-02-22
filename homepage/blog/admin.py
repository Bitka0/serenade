# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from models import Entry, Group, Tag, Comment
from django.contrib import admin
from django.contrib.auth.models import User

class EntryAdmin(admin.ModelAdmin):#
	# Detail display

	# Automatically fill the url field based on what's given as title.
	prepopulated_fields = {'url': ('title',)}

	
	# List display
	
	list_display = ('title', 'url', 'lastModified')
	# Fields in which should be searched.
	search_fields = ['title', 'url', 'text']


class Groupadmin(admin.ModelAdmin):
	list_display= ('name',)

class Tagadmin(admin.ModelAdmin):
	list_display= ('name',)

admin.site.register(Entry, EntryAdmin)
admin.site.register(Group, Groupadmin)
admin.site.register(Tag, Tagadmin)
admin.site.register(Comment)
