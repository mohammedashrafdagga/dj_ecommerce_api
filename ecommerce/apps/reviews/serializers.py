from ecommerce.apps.orders.models import OrderItem
from rest_framework import serializers

from .models import Review


class ReviewSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.username")

    class Meta:
        model = Review
        fields = ("created_by", "rating", "comment", "create_at")


class ReviewCreateSerializer(serializers.ModelSerializer):
    order_item = serializers.PrimaryKeyRelatedField(queryset=OrderItem.objects.all())

    class Meta:
        model = Review
        fields = ["order_item", "rating", "comment"]

    def validate(self, data):
        order_item = data.get("order_item")
        user = self.context["request"].user

        # Ensure the user is the one who made the order
        if order_item.order.owner != user:
            raise serializers.ValidationError(
                "You can only review products you have ordered."
            )

        # Ensure no duplicate review for the same order item
        if Review.objects.filter(order_item=order_item).exists():
            raise serializers.ValidationError(
                "You have already reviewed this order item."
            )

        return data

    def create(self, validated_data):
        order_item = validated_data["order_item"]
        product = order_item.product
        user = self.context["request"].user

        review = Review.objects.create(
            created_by=user,
            product=product,
            order_item=order_item,
            rating=validated_data["rating"],
            comment=validated_data["comment"],
        )
        return review
