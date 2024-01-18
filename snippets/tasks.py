from celery import shared_task
from pastebin.settings import redis_instance
from .models import Snippet


@shared_task
def transfer_data_to_db():
    data = redis_instance.hgetall("snippets_views")
    if data:
        redis_instance.delete("snippets_views")
        objs = []
        for pk, value in data.items():
            obj = Snippet.objects.get(id=pk)
            obj.views += int(value)
            objs.append(obj)
        Snippet.objects.bulk_update(objs, ["views"])


@shared_task
def increment_views(snippet_id):
    redis_instance.hincrby("snippets_views", str(snippet_id))
