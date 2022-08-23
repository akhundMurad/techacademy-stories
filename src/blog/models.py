from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(
        max_length=128,
        null=False,
        verbose_name="title",
    )
    image = models.ImageField(upload_to="posts/%Y/%m/%d", null=True)
    data = models.TextField()
    tags = models.ManyToManyField(
        "blog.Tag",
    )
    author = models.ForeignKey(
        "users.User", related_name="posts", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(
        "blog.Category",
        on_delete=models.CASCADE,
        related_name="posts",
    )

    @property
    def category_name(self):
        return self.category.name

    @property
    def image_url(self) -> str | None:
        if self.image and hasattr(self.image, "url"):
            return self.image.url
        return None

    @property
    def detail_url(self) -> str:
        return reverse("blog:post-detail", kwargs={"pk": self.pk})

    class Meta:
        indexes = [models.Index(fields=["title"])]


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Category(models.Model):
    name = models.CharField(max_length=128)

    class Meta:
        verbose_name_plural = "categories"
