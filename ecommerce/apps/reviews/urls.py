from django.urls import path

from .views import ReviewCreateAPIView, ReviewListAPIView

app_name = "api-reviews"

urlpatterns = [
    path("create/", ReviewCreateAPIView.as_view(), name="create-review"),
    path(
        "product/<int:product_id>/", ReviewListAPIView.as_view(), name="product-reviews"
    ),
]
