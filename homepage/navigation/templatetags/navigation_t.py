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
	
	def addmenu(self, parentid = None):
		entrylist = Entry.objects.all().filter(menu__menuname = self.menu, parent__id = parentid)
		self.menuhtml += '<ul>'
		for entry in entrylist:
			self.menuhtml  += '<li><a href="{0}">{1}</a></li>'.format(entry.target, entry.name)
			if entry.children.count() != 0:
				self.addmenu(entry.id)
		self.menuhtml  += '</ul>'
	
	def render(self, context):
		self.menuhtml = ''
		self.addmenu()
		return self.menuhtml

class SimpleMenuOneNode(Node):
	def __init__(self, menu=None, parent=None):
		if menu != None:
			self.menu = menu
		else:
			self.menu = 1
		
		if parent != None:
			self.parent = parent
		else:
			self.parent = None
	
	def render(self, context):
		entrylist = Entry.objects.all().filter(menu__menuname = self.menu, parent__id = self.parent)
		menuhtml = '<ul>'
		for entry in entrylist:
			menuhtml  += '<li><a href="{0}">{1}</a></li>'.format(entry.target, entry.name)
		menuhtml  += '</ul>'
		return menuhtml

class CheckMenuNode(Node):
    def render(self, context):
        return ''

def simpleMenu(parser, token):
	try:
		tag_name, menu = token.split_contents()
	except:
		menu = None
	return SimpleMenuNode(menu)

def simpleMenuOne(parser, token):
	parent = None
	menu = None
	try:
		content = token.split_contents()
	except:
		menu = None
	
	if len(content) > 1:
		if len(content) > 2:
			menu = content[1]
			parent = content[2]
		else:
			menu = content[1]
	return SimpleMenuOneNode(menu, parent)

def checkMenu(parser, token):
	try:
		tag_name, menu = token.split_contents()
	except:
		menu = None
	entrylist = Entry.objects.all().filter(menu__menuname = menu)
	if entrylist == []:
		parser.skip_past('endcheckMenu')
	return CheckMenuNode()


simpleMenu = register.tag(simpleMenu)
simpleMenuOne = register.tag(simpleMenuOne)
checkMenu = register.tag(checkMenu)
