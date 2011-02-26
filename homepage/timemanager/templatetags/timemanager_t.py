# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.template import Library, Node
from homepage.timemanager.models import Entry

register = Library()

class TmSidebarNode(Node):
	def render(self, context):
		entrylist = Entry.objects.all().filter(published = True)
		calendar = '<ul>'
		for entry in entrylist:
			calendar += '<li>{0} ({1})</li>'.format(entry.name, entry.startDay)
		calendar += '</ul>'
		return calendar

def tmSidebar(parser, token):
	return TmSidebarNode()

tmSidebar = register.tag(tmSidebar)
