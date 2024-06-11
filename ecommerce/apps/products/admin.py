from django.contrib import admin

from .models import Brand, Category, Product, ProductImage


# register Category
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "create_at", "update_at"]
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    readonly_fields = ("create_at", "update_at")


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "create_at", "update_at")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    readonly_fields = ("create_at", "update_at")
    filter_horizontal = ("categories",)  # To use a better UI for ManyToManyField


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "slug", "price", "stock", "category", "brand")
    prepopulated_fields = {"slug": ("name",)}
    search_fields = ("name",)
    list_filter = ("category", "brand", "create_at")
    readonly_fields = ("create_at", "update_at")
    inlines = [ProductImageInline]


@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display = ("product", "image", "create_at")
    readonly_fields = ("create_at",)
