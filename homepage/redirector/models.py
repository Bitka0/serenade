# coding: utf-8 

# Copyright (c) 2011 Lukas Martini, Phillip Thelen.
# This file may be used and distributed under the terms found in the
# file COPYING, which you should have received along with this
# program. If you haven't, please refer to bofh@junge-piraten.de.


from django.db import models

class Redirect(models.Model):
	url = models.SlugField('URL', max_length=200, help_text = 'The local URL which should be redirected.')
	target = models.CharField(max_length=200)

	def __unicode__(self):
		return '{0} -> {1}'.format(self.url, self.target)
