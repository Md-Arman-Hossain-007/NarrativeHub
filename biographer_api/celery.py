import os

from celery import Celery
from django.conf import settings

# TODO: change this in production
os.environ.setdefault(
    key="DJANGO_SETTINGS_MODULE", value="biographer_api.settings.local"
)

app = Celery("biographer_api")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
