from ast import Sub, Subscript
from email.message import EmailMessage
from django.http.response import Http404

from mails.models import Subscription
from blog.models import Category


def subscribe_to_category(email: str, category_id: int) -> None:
    if not Category.objects.filter(id=category_id).exists():
        raise Http404("Category with that id was not found.")

    subscription, _ = Subscription.objects.get_or_create(category_id=category_id)

    if email not in subscription.emails:
        subscription.emails.append(email)
        subscription.save()
