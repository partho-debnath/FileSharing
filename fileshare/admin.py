from django.contrib import admin

from . models import File

# Register your models here.


@admin.register(File)
class AdminFile(admin.ModelAdmin):

    list_display = ['file', 'datetime', 'id']
    list_filter = ['datetime', ]