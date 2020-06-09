import os
from celery import Celery

from tauth.settings import DEBUG

if DEBUG:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tauth.settings')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tauth.production_settings')
app = Celery('tauth')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()