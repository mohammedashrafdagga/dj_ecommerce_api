from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "api/accounts/", include("ecommerce.apps.accounts.urls", namespace="accounts")
    ),
    path(
        "api/products/",
        include("ecommerce.apps.products.urls", namespace="api-product"),
    ),
    path(
        "api/orders/",
        include("ecommerce.apps.orders.urls", namespace="api-orders"),
    ),
    path(
        "api/reviews/",
        include("ecommerce.apps.reviews.urls", namespace="api-reviews"),
    ),
    path(
        "api/notifications/",
        include("ecommerce.apps.notifications.urls", namespace="api-notifications"),
    ),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/schema/docs/", SpectacularSwaggerView.as_view(url_name="schema")),
]

# adding media urls
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
