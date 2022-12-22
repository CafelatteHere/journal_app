from django import forms
from .models import Post

class PostUpdateForm(forms.ModelForm):
  class Meta:
    model = Post
    fields = ["title", "text", "image", "audio", "video", "rubric", "private"]