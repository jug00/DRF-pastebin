import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'pastebin.settings')
app = Celery('pastebin')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

app.conf.beat_schedule = {
    'transfer-data-to-database-and-clear-redis': {
        'task': 'snippets.tasks.transfer_data_to_db',
        'schedule': crontab(minute='*/5'),
    },
}
