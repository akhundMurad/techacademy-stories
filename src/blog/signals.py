from django.db.models import signals
from django.dispatch import receiver

from blog.models import Tag


@receiver(signals.post_delete, sender=Tag)
def handle_tag_deleted(instance: Tag, *args, **kwargs) -> None:
    print(f"Tag({instance.name} was deleted.)")


@receiver(signals.post_migrate)
def handle_post_migrate(*args, **kwargs) -> None:
    print("Migratins were accepted!")
