from django.shortcuts import render
from django.views.generic import ListView

from blog.models import Post


class PostsListView(ListView):
    model = Post
