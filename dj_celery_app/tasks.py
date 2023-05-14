from celery import shared_task
import time


@shared_task
def mock_task(num=15):
    time.sleep(num)
    return f"Slept for {num} seconds"
