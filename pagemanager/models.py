from django.db import models

class Page(models.Model):
	url = models.CharField(max_length=200)

	title = models.CharField(max_length=200)
	comment = models.TextField()
	text = models.TextField()

	def __unicode__(self):
		return "{0} ({1})".format(self.title, self.url)
