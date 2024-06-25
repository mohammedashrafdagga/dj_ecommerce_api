from django.contrib import admin

from .models import Notification

# Register your models here.


class NotificationAdmin(admin.ModelAdmin):
    list_display = ("user", "create_at", "is_read")
    readonly_fields = ("create_at",)


admin.site.register(Notification, NotificationAdmin)
