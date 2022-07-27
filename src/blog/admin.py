from typing import Any
from django.contrib import admin
from django.db.models import QuerySet

from blog import models


class CategoryListFilter(admin.SimpleListFilter):
    title = "category"
    parameter_name = "category"

    def lookups(self, request: Any, model_admin: Any) -> list[tuple[Any, str]]:
        category_ids = model_admin.get_queryset(
            request
        ).values_list(
            "category_id", flat=True
        )
        lookups = []

        for category_id in category_ids:
            lookups.append(
                (
                    category_id, f"Category with id = {category_id}"
                )
            )

        return lookups

    def queryset(self, request: Any, queryset: QuerySet) -> QuerySet | None:
        value = self.value()
        if value:
            queryset = queryset.filter(category_id=value)
        return queryset



class PostModelAdmin(admin.ModelAdmin):
    exclude = ["category", "tags"]
    fieldsets = (
        (
            "Text Fields", {
                "fields": ("title", "data")
            }
        ),
        (
            "Other", {
                "fields": ("image", "author", "created_at")
            }
        )
    )
    list_display = (
        "title",
        "data",
        "created_at",
        "category"
    )
    list_filter = ("created_at", "title", CategoryListFilter)
    readonly_fields = ("created_at",)


class TagModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.Post, PostModelAdmin)
admin.site.register(models.Tag, TagModelAdmin)
admin.site.register(models.Category, CategoryModelAdmin)
