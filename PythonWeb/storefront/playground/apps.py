from django.apps import AppConfig

# Here we configure the application
# NAME IS MISLEADING, NAME SHOULD BE CONFIG.PY

class PlaygroundConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'playground'
