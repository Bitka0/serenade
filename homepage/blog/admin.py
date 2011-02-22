# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from models import Entry, Group, Tag, Comment
from django.contrib import admin
from django.contrib.auth.models import User

class EntryAdmin(admin.ModelAdmin):
	# Detail display

	fieldsets = [
		(None,						{'fields': ['title', 'created_by']}),
		(None,						{'fields': ['text']}),
		(_('Categorisation'),		{'fields': ['groups', 'tags'], 'classes': ['collapse open']}),
		(_('Further options'),		{'fields': ['url', 'admincomment'], 'classes': ['collapse closed']}),
	]

	# Automatically fill the url field based on what's given as title.
	prepopulated_fields = {'url': ('title',)}

	# List display
	list_display = ('title', 'url', 'created_by', 'lastModified')
	# Fields in which should be searched.
	search_fields = ['title', 'url', 'text']
	
	class Media:
		js = ['/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', '/static/grappelli/tinymce_setup/tinymce_setup.js',]

class Commentadmin(admin.ModelAdmin):
	list_display = ('sender', 'subject', 'date')

class Groupadmin(admin.ModelAdmin):
	list_display= ('name',)

class Tagadmin(admin.ModelAdmin):
	list_display= ('name',)

admin.site.register(Entry, EntryAdmin)
admin.site.register(Group, Groupadmin)
admin.site.register(Tag, Tagadmin)
admin.site.register(Comment, Commentadmin)
