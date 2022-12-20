from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from .models import Post, RUBRIC_CHOICES
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView, DeleteView

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

class PostUpdate(UpdateView):
  model = Post
  template_name = 'journal/post_update.html'
  fields = "__all__"
  success_url = '/journal/my_posts/'

class PostDelete(DeleteView):
  model = Post
  template_name = 'journal/post_delete.html'
  success_url = reverse_lazy('my_posts')
