from celery import shared_task
from celery.result import AsyncResult
from dj_celery import celery_app
import time


@shared_task
def mock_task(num=15):
    time.sleep(num)
    return f"Slept for {num} seconds"


def get_result_by_id(task_id):
    res = AsyncResult(task_id, app=celery_app)
    if res.status is not "PENDING":
        return res.get()
    return None
