import time
from datetime import date

from celery import shared_task
from django.contrib.auth import get_user_model
from django_celery_beat.models import PeriodicTask


UserModel = get_user_model()


@shared_task
def send_mails(emails: list[str]) -> None:
    print("Started...")
    time.sleep(3)
    print("End.")


@shared_task
def send_congratulations() -> None:
    print("Starting send congrats...")
    today = date.today()
    for user in UserModel.objects.filter(date_joined__date=today).iterator():
        print(f"Congrats to {user.username}")
