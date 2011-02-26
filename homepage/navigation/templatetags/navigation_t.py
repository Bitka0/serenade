# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.template import Library, Node
from homepage.navigation.models import Entry

register = Library()

class SimpleMenuNode(Node):
	def render(self, context):
		return "Nothing yet"

def simpleMenu(parser, token):
	return SimpleMenuNode()

simpleMenu = register.tag(simpleMenu)
