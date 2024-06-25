from django.db.models.signals import post_save
from django.dispatch import receiver
from ecommerce.apps.notifications.models import Notification

from .models import Order


# create notification when create new order
@receiver(post_save, sender=Order)
def create_notification_for_order(sender, instance, created, **kwargs):

    if created:

        Notification.objects.create(
            user=instance.owner,
            message=f"You are creating a new order at {instance.order_date.date()}",
        )
