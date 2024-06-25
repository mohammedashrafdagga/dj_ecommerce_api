from django.apps import AppConfig


class OrdersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "ecommerce.apps.orders"

    def ready(self) -> None:
        import ecommerce.apps.orders.signals
