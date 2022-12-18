from django.urls import path
from . import views

urlpatterns = [
  path('my_posts/', views.posts_list, name='my_posts'),
  path('create_post/', views.create_post, name="create_post")
]