from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        verbose_name="title"
    )
    data = models.TextField()
    tags = models.ManyToManyField(
        "blog.Tag",
    )
    author = models.ForeignKey(
        "users.User",
        related_name="posts",
        on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


class Tag(models.Model):
    name = models.CharField(max_length=64)
