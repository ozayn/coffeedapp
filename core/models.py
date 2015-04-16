from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.

class Location(models.Model):
	title = models.CharField(max_length = 300) 
	# a character field, maximum of 300 characters
	description = models.TextField(null = True, blank = True) 
	# this field is allowed to be left empty
	created_at = models.DateTimeField(auto_now_add = True) 
	# record the time when this location was created at / automatically add
	address = models.TextField(null = True, blank = True)
	hours = models.TextField(null = True, blank = True)

	def __unicode__(self):  # give titles to locations
		return self.title
         # the instance of location is its own title
 	def get_absolute_url(self):
 		return reverse(viewname="location_list", args=[self.id])