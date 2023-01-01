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
        filename = 'mediafiles\{}--{}.{}'.format(local_time.date(), time, file_extrention)
    return filename


class File(models.Model):
    
    file = models.FileField(upload_to=content_file_name)
    datetime = models.DateTimeField(default=timezone.now()+timezone.timedelta(days=7))
    id = models.PositiveBigIntegerField(primary_key=True)

    def save(self, *args, **kwargs):

        '''
        check this because when an html frontend user use this app, the id field value is not provideed
        manualy so self.id value is None, if self.id is None then add a value inside this if statement. 
        But when an api user use this app, inside 'api.views' -> class 'FileReceiveView' id is provided in 
        "FileSerializer" class and save this value in the database using "FileSerializer", at this time in 
        "save" function self.id is not None because id is already provided in "FileReceiveView" class 
        and this id is not overriden by this "save" function. 
        '''

        if self.id is None: 
            self.id = randint(111111, 999999)
        super(File, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.datetime) + "  " + str(self.file)
