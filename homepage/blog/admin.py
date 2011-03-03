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

class EntryAdmin(admin.ModelAdmin):
	def makePublished(self, request, queryset):
		rows_updated = queryset.update(published = True)
		if rows_updated == 1:
			message_bit = _("1 entry was")
		else:
			message_bit = _("{0} entries were").format(rows_updated)
		self.message_user(request, _("{0} successfully marked as published.").format(message_bit))
	makePublished.short_description = _('Publish selected entries')
	
	def makeDraft(self, request, queryset):
		rows_updated = queryset.update(published = False)
		if rows_updated == 1:
			message_bit = _("1 entry was")
		else:
			message_bit = _("{0} entries were").format(rows_updated)
		self.message_user(request, _("{0} successfully marked as draft.").format(message_bit))
	makeDraft.short_description = _('Unpublish selected entries')
	
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
	
	filter_horizontal = ('groups', 'tags')
	
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
