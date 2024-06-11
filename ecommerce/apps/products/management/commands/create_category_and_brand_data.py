from django.core.management.base import BaseCommand
from django.utils.text import slugify
from ecommerce.apps.products.models import Brand, Category
from faker import Faker


class Command(BaseCommand):
    help = "Generate fake data for category and brand "

    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(10):
            category_name = fake.unique.word().capitalize()
            Category.objects.create(
                name=category_name, content=fake.text(), slug=slugify(category_name)
            )

        # Create fake brands and assign them to random categories
        categories = list(Category.objects.all())

        for _ in range(10):
            brand_name = fake.unique.company()
            brand = Brand.objects.create(
                name=brand_name, content=fake.text(), slug=slugify(brand_name)
            )
            brand.categories.set(fake.random_elements(elements=categories, length=3))

        self.stdout.write(self.style.SUCCESS("Successfully generated fake data"))
