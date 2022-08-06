import logging

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

from blog.services.posts import list_post


logger = logging.getLogger(__name__)


def home(request: HttpRequest) -> HttpResponse:
    if "subscribed_to_category" in request.COOKIES:
        logger.warning("Subcribed to category.", request.COOKIES["subscribed_to_category"])
    logger.warning(request.session.get("subscribed_email"))
    posts = list_post()
    return render(request, "blog/home.html", context={"posts": posts})
