from django.db import models
from django.contrib.auth.models import User

RUBRIC_CHOICES = [
  ("No rubric", "No rubric"),
  ("Daily life", "Daily life"),
  ("Travel", "Travel"),
  ("Sport", "Sport"),
  ("News", "News"),
  ("Food", "Food"),
  ("Discussion", "Discussion"),
  ("Other", "Other")
]
# Create your models here.
class Post(models.Model):
  title = models.CharField(max_length=500)
  text = models.TextField(max_length=2000, null=True, blank=True)
  owner = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
  #storing the link to media files in CharField
  image = models.CharField(max_length=500, null=True, blank=True)
  audio = models.CharField(max_length=500, null=True, blank=True)
  video = models.CharField(max_length=500, null=True, blank=True)
  rubric = models.CharField(max_length=100, default="No rubric", choices=RUBRIC_CHOICES)
  private = models.BooleanField(default=False)

  def __str__(self):
    return self.title
