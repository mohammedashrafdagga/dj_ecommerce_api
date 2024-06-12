import random

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from ecommerce.apps.accounts.models import Account
from ecommerce.apps.orders.models import Order, OrderItem
from ecommerce.apps.products.models import Product
from faker import Faker

User = get_user_model()
fake = Faker()


class Command(BaseCommand):
    help = "Generate fake data for orders and order items"

    def handle(self, *args, **kwargs):

        users = [
            Account.objects.create_user(
                username=fake.user_name(),
                name=fake.name(),
                email=fake.email(),
                password="password",
            )
            for _ in range(5)
        ]

        # Get all Product
        products = list(Product.objects.all())
        order_status = Order.OrderStatus.choices
        # Generate fake orders
        for _ in range(20):
            owner = random.choice(users)
            order = Order.objects.create(owner=owner, total_price=0.0, total_quantity=1)

            # Generate fake order items
            num_items = random.randint(1, 5)
            for _ in range(num_items):
                product = random.choice(products)
                quantity = random.randint(1, 5)
                total_price = quantity * product.price

                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=quantity,
                    total_price=total_price,
                )

            # Update order totals
            order.total_quantity = sum(item.quantity for item in order.items.all())
            order.total_price = sum(item.total_price for item in order.items.all())
            order.save()

        self.stdout.write(self.style.SUCCESS("Successfully generated fake data!"))
