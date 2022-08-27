# Generated by Django 4.0.5 on 2022-08-27 14:18

from django.db import migrations


def forward(apps, schema_editor) -> None:
    Tag = apps.get_model("blog", "Tag")
    TagOfPost = apps.get_model("blog", "TagOfPost")

    tags_of_posts: list[TagOfPost] = []

    for item in Tag.post_set.through.objects.values("tag_id", "post_id"):
        tags_of_posts.append(
            TagOfPost(
                tag_id=item["tag_id"],
                post_id=item["post_id"]
            )
        )

    TagOfPost.objects.bulk_create(tags_of_posts)


def backward(apps, schema_editor) -> None:
    ...


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_tagofpost'),
    ]

    operations = [
        migrations.RunPython(
            code=forward,
            reverse_code=backward
        )
    ]
