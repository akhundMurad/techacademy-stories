from urllib.parse import urlencode, quote_plus
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from django.contrib.auth import get_user_model

from users.forms import UserRegisterForm
from users.services.user import create_user_if_not_exist
from stories.oauth import oauth


UserModel = get_user_model()


def register_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})


def login_user(request: HttpRequest) -> HttpResponse:
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("users:auth-callback"))
    )


def auth_callback(request: HttpRequest) -> HttpResponse:
    user: dict = oauth.auth0.authorize_access_token(request)

    create_user_if_not_exist(
        first_name=user["userinfo"]["given_name"],
        last_name=user["userinfo"]["family_name"],
        email=user["userinfo"]["email"]
    )

    request.session["user"] = user
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
