# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.

from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from grappelli.dashboard import modules, Dashboard
from grappelli.dashboard.utils import get_admin_site_name

class CustomIndexDashboard(Dashboard):
	def init_with_context(self, context):
		site_name = get_admin_site_name(context)
		
		# append a group for "Administration" & "Applications"
		self.children.append(modules.AppList(
			_('General'),
			column=1,
			css_classes = ('collapse open',),
			models = ('homepage.*', 'django.contrib.flatpages.*'),
		))
				
		self.children.append(modules.AppList(
			_('Administration'),
			column=1,
			css_classes = ('collapse open',),
			models = ('django.contrib.*',),
			exclude = ('django.contrib.flatpages.*',),
		))		
				
		# append another link list module for "support".
		self.children.append(modules.LinkList(
			_('Support'),
			column=2,
			children=[
				{
					'title': _('Young Pirates Helpdesk'),
					'url': 'http://helpdesk.junge-piraten.de/',
					'external': True,
				},
				{
					'title': _('Django Documentation'),
					'url': 'http://docs.djangoproject.com/',
					'external': True,
				},
				{
					'title': _('Grappelli Documentation'),
					'url': 'http://packages.python.org/django-grappelli/',
					'external': True,
				},
			]
		))
		
		# append a feed module
		self.children.append(modules.Feed(
			_('Latest wiki edits'),
			column=2,
			feed_url='http://wiki.junge-piraten.de/w/index.php?title=Spezial:Letzte_%C3%84nderungen&feed=rss',
			limit=5
		))
		
		# append a recent actions module
		self.children.append(modules.RecentActions(
			_('Recent Actions'),
			limit=10,
			collapsible=False,
			column=3,
		))


