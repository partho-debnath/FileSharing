from django.db import models
from django.utils import timezone

from random import randint


from . utils import content_file_name


# Create your models here.


class UserIPAddress(models.Model):
    ipaddress = models.GenericIPAddressField()

    def __str__(self):
        return str(self.ipaddress)


class File(models.Model):
    
    file = models.FileField(upload_to=content_file_name)
    datetime = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=7))
    id = models.PositiveBigIntegerField(primary_key=True)

    def save(self, *args, **kwargs):
        self.id = randint(111111, 999999)
        super(File, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.datetime) + "  " + str(self.file)
