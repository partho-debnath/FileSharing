from django.db import models

# Create your models here.


class UserIPAddress(models.Model):
    ipaddress = models.GenericIPAddressField()

    def __str__(self):
        return str(self.ipaddress)

class File(models.Model):
    
    file = models.FileField(upload_to='mediafiles')
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.datetime) + "  " + str(self.file)
