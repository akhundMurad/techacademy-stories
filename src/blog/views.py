from django.views import generic
from django.db.models import Count

from blog.models import Category, Post, Tag
from users.permissions import LoginRequiredMixin


class HomeView(generic.ListView):
    model = Post
    context_object_name = "posts"

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"

    def get_context_data(self, **kwargs) -> dict:
        context_data = super().get_context_data(**kwargs)

        post_tags = self.object.tags.values_list("name", flat=True)
        categories = Category.objects.filter(
            posts__isnull=False
        ).annotate(posts_count=Count("posts")).values(
            "posts_count", "name"
        )
        tags_cloud = Tag.objects.annotate(
            posts_count=Count("post")
        ).order_by("-posts_count").values_list("name")[:3]

        context_data["actual_categories"] = categories
        context_data["post_tags"] = post_tags
        context_data["tags_cloud"] = tags_cloud

        return context_data


class PostCreateView(LoginRequiredMixin, generic.CreateView):
    model = Post
    fields = ["title", "data", "image"]
    template_name_suffix = "_create"
