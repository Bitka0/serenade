# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.template import Library, Node
from homepage.timemanager.models import Entry
from datetime import date

register = Library()

class TmSidebarNode(Node):
	def render(self, context):
		today = date.today()
		entrylist = Entry.objects.all().filter(published = True, startDay__gte = today)
		calendar = '<ul>'
		for entry in entrylist:
			calendar += '<li><a href="/calendar/show/{0}">{1}</a> ('.format(entry.url, entry.name)
			diff = entry.startDay - today
			if diff.days == 0:
				dates = 'today'
			elif diff.days == 1:
				dates = 'tomorrow'
			else:
				dates = '{0}'.format(entry.startDay)
			calendar += dates
			calendar += ')</li>'
		calendar += '</ul><a href="/calendar/">'
		calendar += 'More...'
		calendar += '</a>'
		return calendar

def tmSidebar(parser, token):
	return TmSidebarNode()

tmSidebar = register.tag(tmSidebar)
