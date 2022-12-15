from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=500)
  text = models.TextField(max_length=2000, null=True, blank=True)
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  #storing the link to media files in CharField
  image = models.CharField(max_length=500, null=True, blank=True)
  audio = models.CharField(max_length=500, null=True, blank=True)
  video = models.CharField(max_length=500, null=True, blank=True)