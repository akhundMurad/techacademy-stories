import pytest

from blog.models import Category, Post
from blog import admin


@pytest.fixture
def unused_category(db):
    return Category.objects.create(name="unused_category")


def test_category_list_filter_return_correct_post(post, category, unused_category) -> None:
    filter = admin.CategoryListFilter(
        request=None, 
        params={"category": category.id}, 
        model=Post, 
        model_admin=admin.PostModelAdmin
    )

    queryset = filter.queryset(request=None, queryset=Post.objects.all())

    assert queryset.count() == 1

    assert queryset.first().id == post.id

    filter = admin.CategoryListFilter(
        request=None, 
        params={"category": unused_category.id}, 
        model=Post, 
        model_admin=admin.PostModelAdmin
    )

    queryset = filter.queryset(request=None, queryset=Post.objects.all())

    assert queryset.count() == 0


def test_category_list_filter_return_used_categories(post, category, unused_category) -> None:
    filter = admin.CategoryListFilter(
        request=None, 
        params={"category": category.id}, 
        model=Post, 
        model_admin=admin.PostModelAdmin
    )

    lookups = filter.lookups(request=None, queryset=Post.objects.all())

    assert lookups == [
        (unused_category.id, f"Category with id = {unused_category.id}")
    ]
