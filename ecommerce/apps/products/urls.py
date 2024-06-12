from django.urls import path

from .views import BrandListView, CategoryListView, ProductListView

app_name = "api-product"
urlpatterns = [
    path("", ProductListView.as_view(), name="products-list"),
    path("categories/", CategoryListView.as_view(), name="categories-list"),
    path("brands/", BrandListView.as_view(), name="brands-list"),
]
