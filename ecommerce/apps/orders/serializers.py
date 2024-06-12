from ecommerce.apps.products.models import Product
from ecommerce.apps.products.serializers import ProductSerializer
from rest_framework import serializers

from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer()

    class Meta:
        model = OrderItem
        fields = ["id", "product", "quantity", "total_price"]


class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = (
            "id",
            "owner",
            "order_date",
            "total_price",
            "total_quantity",
            "status",
            "items",
        )
        read_only_fields = [
            "owner",
            "order_date",
            "total_price",
            "total_quantity",
            "status",
        ]


#  for creating Order and related items
class OrderCreateSerializer(serializers.ModelSerializer):
    # items is list from product with quantity and total price
    items = serializers.ListField(child=serializers.DictField(), write_only=True)

    class Meta:
        model = Order
        fields = ["items"]

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        owner = self.context["request"].user
        order = Order.objects.create(owner=owner)
        total_price = 0
        total_quantity = 0
        for item in items_data:
            product_id = item["product_id"]
            quantity = item["quantity"]
            product = Product.objects.get(pk=product_id)
            price = product.price
            # for Order object
            total_price += price * quantity
            total_quantity += quantity
            OrderItem.objects.create(
                order=order,
                product=product,
                quantity=quantity,
                total_price=price * quantity,
            )
        order.total_price = total_price
        order.total_quantity = total_quantity
        order.save()
        
        return order
