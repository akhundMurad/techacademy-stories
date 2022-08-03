from django.db import models
from django.contrib.postgres.fields import ArrayField


class Subscription(models.Model):
    category = models.OneToOneField(
        "blog.Category", on_delete=models.CASCADE, unique=True
    )
    emails = ArrayField(
        base_field=models.EmailField(max_length=128), size=1000, default=list
    )

    class Meta:
        verbose_name = "subscription"
        verbose_name_plural = "subscriptions"
