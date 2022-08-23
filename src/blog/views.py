from django.views import generic
from django.db.models import QuerySet

from blog.services.posts import list_post
from blog.models import Post
from users.permissions import LoginRequiredMixin


class HomeView(generic.ListView):
    model = Post
    context_object_name = "posts"


class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "data", "image"]
    template_name_suffix = "_create"
