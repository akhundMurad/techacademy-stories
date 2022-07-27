from typing import Type
import pytest

from django.contrib.auth import get_user_model

from blog.models import Category, Tag, Post


@pytest.fixture
def user_model():
    return get_user_model()


@pytest.fixture
def category(db) -> Category:
    return Category.objects.create(name="Category")


@pytest.fixture
def tag(db) -> Tag:
    return Tag.objects.create(name="Tag")


@pytest.fixture
def post(db, category, user_model) -> Post:
    post = Post.objects.create(
        title="Post",
        data="Data",
        author=user_model.objects.create(
            first_name="First",
            last_name="Last",
            password="1872yiuwhd",
            email="email@gmail.com"
        ),
        category=category
    )
    post.tags.add(Tag.objects.create(name="tag"))
    return post