from datetime import timedelta

from django.db.models import QuerySet
from django.utils import timezone

from blog.models import Post


def list_post() -> QuerySet:
    today = timezone.now() - timedelta(days=10)

    return Post.objects.all().order_by("-created_at")
