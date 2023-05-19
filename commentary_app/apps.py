from django.apps import AppConfig


class CommentaryAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "commentary_app"

    def ready(self):
        import commentary_app.signals
