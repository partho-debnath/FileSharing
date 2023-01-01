from django.utils import timezone
from django.conf import settings

from apscheduler.schedulers.background import BackgroundScheduler


from .models import File

# from django.db.models.functions import Now


def deleteExpiredRecords() -> None:
    print('---apps-----')
    File.objects.filter(datetime__lte=timezone.now()).delete()

    return None


def myJobScheduler() -> None:
    scheduler = BackgroundScheduler()
    scheduler.add_job(deleteExpiredRecords, 'interval', days=settings.APP_SCHEDULER_TIME)
    scheduler.start()

    return None