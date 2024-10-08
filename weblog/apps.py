from django.apps import AppConfig


class WeblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weblog'

    def ready(self) -> None:
        from .import signals
