from django.apps import AppConfig


class FileshareConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'fileshare'

    def ready(self) -> None:    # override the ready method
        from .appsheduler import myJobScheduler
        myJobScheduler()

        return None