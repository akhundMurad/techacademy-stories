from datetime import timedelta, datetime

from django.db.models import QuerySet

from blog.models import Post


def list_post() -> QuerySet:
    today = datetime.utcnow() - timedelta(days=10)

    return Post.objects.filter(created_at__gte=today).order_by("-created_at")[2:5]
