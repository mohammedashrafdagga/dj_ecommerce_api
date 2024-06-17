import random

from django.core.management import BaseCommand
from ecommerce.apps.orders.models import OrderItem
from ecommerce.apps.reviews.models import Review
from faker import Faker


class Command(BaseCommand):
    help = "Generate fake data for orders and order items"

    def handle(self, *args, **kwargs):
        orders_item = list(OrderItem.objects.all())
        fake = Faker()

        for order in orders_item:
            rating = random.randint(1, 5)
            comment = fake.text(max_nb_chars=200)
            Review.objects.create(order_item=order, rating=rating, comment=comment)
