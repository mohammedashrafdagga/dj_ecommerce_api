from django.db.models.signals import post_save
from django.dispatch import receiver
from ecommerce.apps.notifications.models import Notification

from .models import Review


@receiver(post_save, sender=Review)
def create_notification_for_review(sender, instance, created, **kwargs):
    if created:
        Notification.objects.create(
            user=instance.created_by,
            message=f" You are making a review for the product is: {instance.product} with a rating is {instance.rating}",
        )
