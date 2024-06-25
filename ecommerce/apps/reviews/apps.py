from django.apps import AppConfig


class ReviewsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.reviews"

    def ready(self) -> None:
        import ecommerce.apps.reviews.signals

        return super().ready()
