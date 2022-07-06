from django.shortcuts import render

from blog.services.posts import list_post


def home(request):
    posts = list_post()

    return render(
        request,
        "blog/home.html",
        context={
            "posts": posts
        }
    )
