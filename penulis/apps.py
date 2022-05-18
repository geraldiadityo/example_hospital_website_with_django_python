from django.apps import AppConfig


class PenulisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'penulis'

    def ready(self):
        import penulis.signals