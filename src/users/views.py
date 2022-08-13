from urllib.parse import urlencode, quote_plus
from authlib.integrations.django_client import OAuth
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth import login
from django.conf import settings
from django.urls import reverse

from users.forms import UserRegisterForm


def register_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})


oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)


def login_user(request: HttpRequest) -> HttpResponse:
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("users:auth-callback"))
    )


def auth_callback(request: HttpRequest) -> HttpResponse:
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    return redirect(request.build_absolute_uri(reverse("blog:home")))


def logout(request: HttpRequest) -> HttpResponse:
    request.session.clear()

    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("blog:home")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )
