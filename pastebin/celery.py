import os
from celery import Celery
from celery.schedules import crontab

# Устанавливаем переменную окружения для настроек Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pastebin.settings")
# Создаем экземпляр Celery с именем 'pastebin'
app = Celery("pastebin")
# Загружаем конфигурацию Celery из настроек Django
app.config_from_object("django.conf:settings", namespace="CELERY")
# Автоматически обнаруживаем задачи в приложениях Django
app.autodiscover_tasks()

# Настраиваем расписание для периодической задачи
app.conf.beat_schedule = {
    "transfer-data-to-database-and-clear-redis": {
        "task": "snippets.tasks.transfer_data_to_db",
        "schedule": crontab(minute="*/5"),
    },
}
