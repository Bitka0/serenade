# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from blog.models import Entry
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Atom1Feed


class blogAll(Feed):
	title = "Blog Feed"
	link = "/blog/"
	description = "Updates on changes and additions."
	feed_type = Atom1Feed
	
	def items(self):
		return Entry.objects.order_by('-publishingDate')[:15]

	def item_title(self, item):
		return item.title

	def item_description(self, item):
		return item.text[:1000]
