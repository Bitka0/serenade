# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from models import Entry
from django.contrib import admin

class EntryAdmin(admin.ModelAdmin):
	list_display = ('name', 'wholeDay')

admin.site.register(Entry, EntryAdmin)
