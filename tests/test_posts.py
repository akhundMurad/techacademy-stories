from datetime import timedelta
from django.contrib.auth import get_user_model
from django.db.models import QuerySet
from django.utils import timezone
import pytest

from blog.models import Post, Tag, Category
from blog.services.posts import list_post


User = get_user_model()


@pytest.fixture
def category() -> Category:
    return Category.objects.create(name="Category")


@pytest.fixture
def tag() -> Tag:
    return Tag.objects.create(name="Tag")


@pytest.fixture
def post(category) -> Post:
    post = Post.objects.create(
        title="Post",
        data="Data",
        author=User.objects.create(
            first_name="First",
            last_name="Last",
            password="1872yiuwhd",
            email="email@gmail.com"
        ),
        category=category
    )
    post.tags.add(Tag.objects.create(name="tag"))
    return post


def test_list_post_return_queryset(db, post) -> None:
    posts = list_post()

    assert isinstance(posts, QuerySet)


def test_list_post_return_created_at_gte_10_days_ago(db, post) -> None:
    post.created_at = timezone.now() - timedelta(days=11)
    post.save()

    posts = list_post()

    assert posts.count() == 0
