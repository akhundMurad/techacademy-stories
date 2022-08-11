from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from users.forms import UserRegisterForm


def register_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/")
    form = UserRegisterForm()
    return render(request, "users/register.html", context={"form": form})


def login_user(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(request=request, data=request.POST)
        if form.is_valid():
            form.clean()
            user = form.get_user()
            login(request, user)
        return HttpResponseRedirect("/")
    form = AuthenticationForm(request)
    return render(request, "users/login.html", context={"form": form})
