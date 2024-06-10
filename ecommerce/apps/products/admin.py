from django.contrib import admin

from .models import Brand, Category


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
