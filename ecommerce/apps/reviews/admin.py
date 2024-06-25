from django.contrib import admin

from .models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        "created_by",
        "product",
        "order_item",
        "rating",
        "create_at",
    )
    list_filter = ("product", "rating")
    search_fields = ("rating", "product__name")
    readonly_fields = ("product", "created_by")


admin.site.register(Review, ReviewAdmin)
