import os

from celery import Celery
from celery.schedules import crontab


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'stories.settings')


app = Celery('stories')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.beat_schedule = {
    'send-congrats': {
        'task': 'tasks.tasks.mails.send_congratulations',
        'schedule': crontab(minute='*/1')
    }
}

app.autodiscover_tasks()
