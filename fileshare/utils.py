import os

from django.conf import settings
from django.utils.timezone import localtime, now

from pathlib import Path

media_storage_name = 'mediafiles'


def get_media_storage_name() -> str:
    return media_storage_name

def getFileNameAsTime(file_extrention:str):
    file_extrention = file_extrention.replace('.', '')
    local_time = localtime(now())
    time = str(local_time.time()).split('.')[0].replace(':', '-')
    media_dir = Path.joinpath(settings.MEDIA_ROOT, media_storage_name)
    filename = Path.joinpath(media_dir, '{}--{}.{}'.format(local_time.date(), time, file_extrention))
    return filename


def content_file_name(instance, filename) -> str:
    file_extrention = filename.split('.')[-1]
    '''
    instance pk is not created yet, because this instance has not been saved yet. 
    '''
    if instance.pk == 1:
        filename = '{}.{}'.format(instance.pk, file_extrention)
    else:
        filename = os.path.join(media_storage_name, str(getFileNameAsTime(file_extrention)).split('/')[-1])
    return filename


def getTemporaryFilePath(file_name:str) -> str:
    file_path = Path.joinpath(settings.MEDIA_ROOT, file_name)
    return str(file_path)
    