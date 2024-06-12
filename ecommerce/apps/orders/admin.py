from django.contrib import admin

from .models import Order, OrderItem


# Register your models here.
class OrderItemInline(admin.TabularInline):
    model = OrderItem
    extra = 1


class OrderAdmin(admin.ModelAdmin):
    list_display = ("owner", "order_date", "total_price", "total_quantity", "status")
    list_filter = ("status", "order_date")
    search_fields = ("owner__name", "owner__email")
    inlines = [OrderItemInline]


admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem)
