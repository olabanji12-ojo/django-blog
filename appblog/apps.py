from django.apps import AppConfig


class AppblogConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'appblog'
    
    def ready(self):
        import appblog.signals
