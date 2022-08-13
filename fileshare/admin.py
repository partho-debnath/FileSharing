from django.contrib import admin

from . models import File, UserIPAddress

# Register your models here.



class AdminUserIPAddress(admin.ModelAdmin):
    list_display = ['ipaddress', ]
    list_filter = ['ipaddress', ]

admin.site.register(UserIPAddress, AdminUserIPAddress)


@admin.register(File)
class AdminFile(admin.ModelAdmin):

    list_display = ['id', 'file', 'datetime']
    list_filter = ['datetime', ]