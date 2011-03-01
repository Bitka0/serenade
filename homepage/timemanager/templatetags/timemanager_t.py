# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.template import Library, Node
from homepage.timemanager.models import Entry

register = Library()

class TmSidebarNode(Node):
	def render(self, context):
		entrylist = Entry.objects.all().filter(published = True)
		calendar = '<ul>'
		for entry in entrylist:
			calendar += '<li><a href="/calendar/show/{0}">{1}</a> ({2})</li>'.format(entry.url, entry.name, entry.startDay)
		calendar += '</ul><a href="/calendar/">'
		calendar += 'More...'
		calendar += '</a>'
		return calendar

def tmSidebar(parser, token):
	return TmSidebarNode()

tmSidebar = register.tag(tmSidebar)
