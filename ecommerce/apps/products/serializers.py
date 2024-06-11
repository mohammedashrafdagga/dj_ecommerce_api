from rest_framework import serializers

from .models import Brand, Category, Product, ProductImage


# for category serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["name", "slug", "content"]


# Brand Image Serializer
class BrandSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)

    class Meta:
        model = Brand
        fields = ["name", "content", "categories"]


# Product Image Serializer
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["id", "image"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    brand = BrandSerializer(read_only=True)
    images = ProductImageSerializer(read_only=True, many=True)

    class Meta:
        model = Product
        fields = [
            "name",
            "slug",
            "content",
            "price",
            "stock",
            "category",
            "brand",
            "main_image",
            "images",
        ]
