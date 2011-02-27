# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from blog.models import Entry
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed
from django.shortcuts import get_object_or_404
import util

class blogAll(Feed):
	title = "Blog Feed"
	link = "/blog/"
	description = "Updates on changes and additions."
	feed_type = Atom1Feed
	
	def items(self):
		return Entry.objects.all()[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.text[:1000]

class selectGroup(Feed):
	link = "/blog/"
	description = "Updates on changes and additions."
	feed_type = Atom1Feed
	
	def title(self):
		return "Blog Feed: {0}".format(self.url)
	
	def link(self):
		return "/blog/group/{0}".format(self.url)
	
	def get_object(self, request, url):
		self.url = util.stripSlash(url)
	
	def items(self):
		return Entry.objects.filter(groups__name = self.url)[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.text[:1000]

class selectTag(Feed):
	link = "/blog/"
	description = "Updates on changes and additions."
	feed_type = Atom1Feed
	
	def title(self):
		return "Blog Feed: {0}".format(self.url)
	
	def link(self):
		return "/blog/tag/{0}".format(self.url)
	
	def get_object(self, request, url):
		self.url = util.stripSlash(url)
	
	def items(self):
		return Entry.objects.filter(tags__name = self.url)[:20]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.text[:1000]
