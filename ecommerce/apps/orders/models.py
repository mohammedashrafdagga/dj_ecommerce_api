from django.db import models
from ecommerce.apps.accounts.models import Account
from ecommerce.apps.products.models import Product


# Order Model
class Order(models.Model):
    class OrderStatus(models.TextChoices):
        PENDING = "Pending"
        COMPLETED = "Completed"
        CANCELLED = "Cancelled"

    owner = models.ForeignKey(Account, related_name="orders", on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(
        max_length=9, default=OrderStatus.PENDING, choices=OrderStatus.choices
    )

    def __str__(self):
        return f"Order {self.id} by {self.owner}"


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, related_name="items", on_delete=models.SET_NULL, null=True, blank=True
    )
    product = models.ForeignKey(
        Product,
        related_name="product_orders",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    quantity = models.PositiveIntegerField(default=1)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    # override the save method to called total price
    def save(self, *args, **kwargs) -> None:
        # calculate the total price
        self.total_price = self.quantity * self.product.price
        return super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f"{self.quantity} x {self.product.name} in Order {self.order.id}"
