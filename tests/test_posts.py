from datetime import timedelta
from django.db.models import QuerySet
from django.utils import timezone

from blog.services.posts import list_post


def test_list_post_return_queryset(post) -> None:
    posts = list_post()

    assert isinstance(posts, QuerySet)


def test_list_post_return_created_at_gte_10_days_ago(post) -> None:
    post.created_at = timezone.now() - timedelta(days=11)
    post.save()

    posts = list_post()

    assert posts.count() == 0
