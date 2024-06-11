import random

from django.core.management.base import BaseCommand
from django.utils.text import slugify
from ecommerce.apps.products.models import Brand, Category, Product, ProductImage
from faker import Faker


class Command(BaseCommand):
    help = "Generate fake data for categories, brands, products, and product images"

    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = list(Category.objects.all())
        brands = list(Brand.objects.all())
        for _ in range(50):
            product_name = fake.unique.word().capitalize()
            product = Product.objects.create(
                name=product_name,
                slug=slugify(product_name),
                content=fake.text(),
                price=round(random.uniform(10.0, 1000.0), 2),
                stock=random.randint(1, 100),
                category=random.choice(categories),
                brand=random.choice(brands),
            )

            # Create fake product images
            for _ in range(random.randint(1, 5)):
                ProductImage.objects.create(product=product)

        self.stdout.write(self.style.SUCCESS("Successfully generated fake data"))
