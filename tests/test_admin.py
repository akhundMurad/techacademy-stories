import site
import pytest

from blog.models import Category, Post
from blog import admin


@pytest.fixture
def unused_category(db):
    return Category.objects.create(name="unused_category")


@pytest.fixture
def post_model_admin() -> admin.PostModelAdmin:
    return admin.PostModelAdmin(Post, site)


def test_category_list_filter_return_correct_post(
    post, 
    category, 
    unused_category, 
    request_factory,
    post_model_admin
) -> None:
    request = request_factory.get("/", {})
    filter = admin.CategoryListFilter(
        request=request, 
        params={"category": category.id}, 
        model=Post, 
        model_admin=post_model_admin
    )

    queryset = filter.queryset(request=request, queryset=Post.objects.all())

    assert queryset.count() == 1

    assert queryset.first().id == post.id

    filter = admin.CategoryListFilter(
        request=request, 
        params={"category": unused_category.id}, 
        model=Post, 
        model_admin=post_model_admin
    )

    queryset = filter.queryset(request=request, queryset=Post.objects.all())

    assert queryset.count() == 0


def test_category_list_filter_return_used_categories(
    post, 
    category, 
    unused_category, 
    request_factory,
    post_model_admin
) -> None:
    request = request_factory.get("/", {})
    filter = admin.CategoryListFilter(
        request=request, 
        params={"category": category.id}, 
        model=Post, 
        model_admin=post_model_admin
    )

    lookups = filter.lookups(request=request, model_admin=post_model_admin)

    assert lookups == [
        (category.id, f"Category with id = {category.id}")
    ]
