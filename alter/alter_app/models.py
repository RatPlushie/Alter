from django.db import models
from django.contrib.auth.models import User

# Create your models here:
class Species(models.Model):
    name = models.CharField(max_length=200)

class Art(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)
    psd_filename = models.TextField()
    species = models.ForeignKey(Species, on_delete=models.DO_NOTHING)
