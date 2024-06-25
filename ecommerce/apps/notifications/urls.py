from django.urls import path

from .views import NotificationListAPIView, NotificationMarkIsReadAPIView

app_name = "api-notifications"

urlpatterns = [
    path("", NotificationListAPIView.as_view(), name="notification-list"),
    path(
        "<int:pk>/read/",
        NotificationMarkIsReadAPIView.as_view(),
        name="notification-mark-as-read",
    ),
]
