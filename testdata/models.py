from django.db import models

# Create your models here.

class Data(models.Model):
	path = models.CharField(max_length=256)
	name = models.CharField(max_length=256)
	data = models.CharField(max_length=40960)
	
	def __str__(self):
		return self.path
	
	class Admin:
		list_display = ('path', 'name')

