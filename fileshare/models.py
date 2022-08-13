from django.db import models

from random import randint

# Create your models here.


class UserIPAddress(models.Model):
    ipaddress = models.GenericIPAddressField()

    def __str__(self):
        return str(self.ipaddress)


class File(models.Model):
    
    file = models.FileField(upload_to='mediafiles')
    datetime = models.DateTimeField(auto_now_add=True)
    id = models.PositiveBigIntegerField(primary_key=True, unique=True)

    def save(self, *args, **kwargs):
        self.id = randint(111111, 999999)
        super(File, self).save(*args, **kwargs)


    def __str__(self):
        return str(self.datetime) + "  " + str(self.file)
