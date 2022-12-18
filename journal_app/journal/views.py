from django.shortcuts import render, redirect
from .models import Post, RUBRIC_CHOICES
from django.contrib.auth.models import User

# Create your views here.
def posts_list(request):
  posts_list = Post.objects.all()
  context = {
    'posts_list': posts_list
  }
  return render(request, 'journal/my_posts.html', context=context)

def create_post(request):
  context = {
    'rubric_choices': RUBRIC_CHOICES
  }

  if request.method == 'POST':
    title = request.POST.get("title", "")
    text = request.POST.get("text", "")
    owner = request.user
    image = request.POST.get("image", "")
    audio = request.POST.get("audio", "")
    video = request.POST.get("video", "")
    rubric = request.POST.get("rubric", "")
    private =  request.POST.get("private", "")
    if private == 'on':
      private =  True
    else:
      private = False

    post = Post(title=title, text=text, owner=owner, image=image, audio=audio, video=video, rubric=rubric, private=private)
    post.save()
    return redirect(posts_list)


  return render(request, 'journal/create_post.html', context=context)