import os
from celery import Celery
from celery.schedules import crontab
from datetime import datetime

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ReportGenerator.settings')

app = Celery('ReportGenerator')


app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()


app.conf.beat_schedule = {
    'run-census-job-every-october': {
        'task': 'census.tasks.process_census_data',
        'schedule': crontab(minute=0, hour=0, day_of_month=1, month_of_year=10),
        'args': ()
    }
}