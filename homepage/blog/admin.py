# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from models import Entry, Group, Tag
from django.contrib import admin
from django.contrib.auth.models import User
from settings import STATIC_URL
from django.contrib.comments.moderation import CommentModerator, moderator

def makePublished(modeladmin, request, queryset):
    queryset.update(published = True)
makePublished.short_description = _('Publish selected blog entries')

def makeDraft(modeladmin, request, queryset):
    queryset.update(published = False)
makeDraft.short_description = _('Unpublish selected blog entries')

class EntryAdmin(admin.ModelAdmin):
	fieldsets = [
		(None,						{'fields': ['title', 'author', 'published']}),
		(None,						{'fields': ['text']}),
		(_('Categorisation'),		{'fields': ['groups', 'tags'], 'classes': ['collapse open']}),
		(_('Further options'),		{'fields': ['url', 'enable_comments', 'admincomment'], 'classes': ['collapse closed']}),
	]

	# Automatically fill the url field based on what's given as title.
	prepopulated_fields = {'url': ('title',)}

	# List display
	list_display = ('title', 'getLink', 'author', 'lastModified', 'published')
	
	list_filter = ['published', 'author']
	date_hierarchy = 'creationDate'
	
	# Fields in which should be searched.
	search_fields = ['title', 'url', 'text']
	
	actions = [makePublished, makeDraft]
	
	# WYSIWTF-Editor
	class Media:
		js = [STATIC_URL + 'grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js', STATIC_URL + 'grappelli/tinymce_setup/tinymce_setup.js',]

class Commentadmin(admin.ModelAdmin):
	list_display = ('sender', 'subject', 'date')

class Groupadmin(admin.ModelAdmin):
	list_display= ('name',)

class Tagadmin(admin.ModelAdmin):
	list_display= ('name',)
	
class EntryModerator(CommentModerator):
    email_notification = False
    enable_field = 'enable_comments'

moderator.register(Entry, EntryModerator)
admin.site.register(Entry, EntryAdmin)
admin.site.register(Group, Groupadmin)
admin.site.register(Tag, Tagadmin)
