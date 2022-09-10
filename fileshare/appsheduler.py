from django.utils import timezone

from apscheduler.schedulers.background import BackgroundScheduler


from .models import File

# from django.db.models.functions import Now


def deleteExpiredRecords() -> None:
    File.objects.filter(datetime__lte=timezone.now()).delete()

    return None


def myJobScheduler() -> None:
    scheduler = BackgroundScheduler()
    scheduler.add_job(deleteExpiredRecords, 'interval', days=1)
    scheduler.start()

    return None