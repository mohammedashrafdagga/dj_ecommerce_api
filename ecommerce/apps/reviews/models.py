from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from ecommerce.apps.accounts.models import Account
from ecommerce.apps.orders.models import OrderItem
from ecommerce.apps.products.models import Product


# Create your models here.
class Review(models.Model):
    # created_by
    created_by = models.ForeignKey(
        Account,
        related_name="reviews",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    product = models.ForeignKey(
        Product, related_name="reviews", on_delete=models.CASCADE
    )
    order_item = models.OneToOneField(OrderItem, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(
                limit_value=1,
                message="The Rating Value Must Be Greater that or equal 1",
            ),
            MaxValueValidator(
                limit_value=5, message="The Rating Value Must Be Less than or equal 5"
            ),
        ],
    )
    #  I want the comment Field is required
    comment = models.TextField()
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f"{self.order_item.id}:// {self.created_by} - {self.rating}"

    # override
    # The Product id is taken from OrderItem
    def save(self, *args, **kwargs) -> None:
        if not self.product:
            self.product = self.order_item.product
        if not self.created_by:
            self.created_by = self.order_item.order.owner
        return super().save(*args, **kwargs)
