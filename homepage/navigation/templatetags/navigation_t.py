# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.template import Library, Node
from homepage.navigation.models import Entry

register = Library()

class SimpleMenuNode(Node):
	def __init__(self, menu=None):
		if menu != None:
			self.menu = menu
		else:
			self.menu = 1
	def render(self, context):
		entrylist = Entry.objects.all().filter(menu = self.menu)
		menu = '<ul>'
		for entry in entrylist:
			menu += '<li><a href="{0}">{1}</a></li>'.format(entry.target, entry.name)
		menu += '</ul>'
		return menu


def simpleMenu(parser, token):
	try:
		tag_name, menu = token.split_contents()
	except:
		menu = None
	return SimpleMenuNode(menu)

simpleMenu = register.tag(simpleMenu)
