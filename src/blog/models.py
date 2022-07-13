from django.db import models


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        verbose_name="title"
    )
    image = models.ImageField(upload_to="uploads/% Y/% m/% d/", null=True)
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
    category = models.ForeignKey("blog.Category", null=True, blank=True, on_delete=models.CASCADE)

    @property
    def category_name(self):
        return self.category.name


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "categories"
