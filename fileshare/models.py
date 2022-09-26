from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime, now

from random import randint

# Create your models here.


class UserIPAddress(models.Model):
    ipaddress = models.GenericIPAddressField()

    def __str__(self):
        return str(self.ipaddress)


def content_file_name(instance, filename):
    file_extrention = filename.split('.')[-1]
    '''
    instance pk is not created yet, because this instance has not been saved yet. 
    '''
    if instance.pk:  
        filename = '{}.{}'.format(instance.pk, file_extrention)
    else:
        local_time = localtime(now())
        time = str(local_time.time()).split('.')[0].replace(':', '-')
        filename = '{}--{}.{}'.format(local_time.date(), time, file_extrention)
    return filename



class File(models.Model):
    
    file = models.FileField(upload_to=content_file_name)
    datetime = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=7))
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)

    def save(self, *args, **kwargs):
        self.id = randint(111111, 999999)
        super(File, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.datetime) + "  " + str(self.file)
