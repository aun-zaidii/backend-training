import logging

from celery import shared_task
from django.utils import timezone

from .models import *
from .service import request_data_for_multiple_years, save_to_db

from .enums import *
from django.db import transaction

logger = logging.getLogger(__name__)


@shared_task(bind=True, ignore_result=True)
def process_census_data(self, years):
    task_log = CensusLog.objects.create(
        task_id=self.request.id, name="fetch_and_save_data", status="in_progress"
    )
    logger.info(f"Starting data processing for years: {years}")
    try:
        with transaction.atomic():
            data = request_data_for_multiple_years(years)
            save_to_db(data)
        task_log.status = StatusChoices.completed
        task_log.finish_at = timezone.now()
        task_log.save()
        logger.info("Data successfully processed and saved to DB.")
    except Exception as e:
        task_log.status = StatusChoices.failed
        task_log.finish_at = timezone.now()
        task_log.log_error = str(e)
        task_log.save()
        logger.error(f"Error processing data: {e}")
        raise ValueError(f"Task failed: {str(e)}")
