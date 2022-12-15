from django.shortcuts import render
from .models import Post
from django.contrib.auth.models import User

# Create your views here.
def posts_list(request):
  posts_list = Post.objects.all()
  context = {
    'posts_list': posts_list
  }
  return render(request, 'journal/my_posts.html', context=context)