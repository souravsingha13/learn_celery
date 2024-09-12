from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# Set default Django settings module for 'celery'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "projectcelery.settings")

app = Celery(
    "projectcelery",
    broker_connection_retry_on_startup=True,
    broker_connection_max_retries=10,
)

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()
