from django.shortcuts import render


def home(request):
    return render(
        request,
        "blog/home.html",
        context={"posts": [{"post_id": 1}]}
    )
