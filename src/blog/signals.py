from django.db.models import signals
from django.dispatch import receiver

from blog.models import Tag
from mails.services import send_mail


@receiver(signals.post_save, sender=Tag)
def handle_tag_created(
    instance: Tag, created: bool, *args, **kwargs
) -> None:
    if created:
        send_mail(instance)


@receiver(signals.post_delete, sender=Tag)
def handle_tag_deleted(instance: Tag, *args, **kwargs) -> None:
    print(f"Tag({instance.name} was deleted.)")


@receiver(signals.post_migrate)
def handle_post_migrate(*args, **kwargs) -> None:
    print("Migratins were accepted!")
