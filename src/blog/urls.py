from django.urls import path
from django.views.decorators.cache import cache_page

from blog.views import HomeView, PostDetailView, PostCreateView


app_name = "blog"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("post/<int:pk>", PostDetailView.as_view(), name="post-detail"),
    path("post/create", PostCreateView.as_view(), name="post-create")
]
