from django.contrib import admin

from blog import models


class PostModelAdmin(admin.ModelAdmin):
    list_display = ("title",)


class TagModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ("name",)


admin.site.register(models.Post, PostModelAdmin)
admin.site.register(models.Tag, TagModelAdmin)
admin.site.register(models.Category, CategoryModelAdmin)
