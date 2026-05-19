from django.apps import AppConfig
 
 
class CoreSignalsConfig(AppConfig):
 
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_signals'
 
    def ready(self):
 
        import core_signals.signals