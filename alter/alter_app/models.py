from django.db import models
from django.contrib.auth.models import User

# Create your models here:
class Species(models.Model):
	name = models.CharField(max_length=200)

class Art(models.Model):
	# TODO foreign keys dont link correctly and cause errors

	author = models.ForeignKey(User, on_delete=models.CASCADE)
	date = models.DateTimeField(auto_now=True)
	title = models.CharField(max_length=200)
	species = models.CharField(max_length=200)
	description = models.TextField()
	file = models.FileField(upload_to='psd/')
	thumbnail = models.FileField(upload_to='thumb/', blank=True, null=True)
	#species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)
	
