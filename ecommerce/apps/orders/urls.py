from django.urls import path

from .views import OrderCreateAPIView, OrderDetailView, OrderListAPIView

app_name = "api-orders"
urlpatterns = [
    path("", OrderListAPIView.as_view(), name="list"),
    path("create/", OrderCreateAPIView.as_view(), name="create"),
    path("<int:pk>/", OrderDetailView.as_view(), name="detail"),
]
