from django.apps import AppConfig


class AlterAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'alter_app'
