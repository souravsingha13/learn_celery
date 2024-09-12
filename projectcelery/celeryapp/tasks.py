# myapp/tasks.py
from celery import shared_task

@shared_task(name="printing nothing", bind=True, retry_kwargs={"max_retries": 10})
def nothing():
    print("Printing nothing.")