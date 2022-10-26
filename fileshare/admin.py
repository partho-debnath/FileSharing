from django.contrib import admin
from django.contrib.auth.models import Group

from . models import File, UserIPAddress


# Unregister Group models here.
admin.site.unregister(Group)



# Register your models here.

class AdminUserIPAddress(admin.ModelAdmin):
    list_display = ['ipaddress', ]
    list_filter = ['ipaddress', ]

admin.site.register(UserIPAddress, AdminUserIPAddress)


@admin.register(File)
class AdminFile(admin.ModelAdmin):

    list_display = ['id', 'file', 'datetime']
    list_filter = ['datetime', ]