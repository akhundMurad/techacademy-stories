from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse, HttpResponseRedirect

from mails.forms import SubscribeToNewletter
from mails.services import subscribe_to_category


def subscribe(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = SubscribeToNewletter(request.POST)
        if form.is_valid():
            subscribe_to_category(
                email=form.cleaned_data["email"],
                category_id=form.cleaned_data["category"].id,
            )
            return HttpResponseRedirect("/")
    else:
        form = SubscribeToNewletter()

    return render(request, "mails/subscribe.html", {"form": form})
