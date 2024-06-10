from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    AccountCreateView,
    AccountDetailView,
    AccountUpdateView,
    ChangePasswordView,
)

app_name = "accounts"

urlpatterns = [
    path("create-account/", AccountCreateView.as_view(), name="create-account"),
    path("login/", TokenObtainPairView.as_view(), name="login"),
    path("login/refresh/", TokenRefreshView.as_view(), name="login_refresh"),
    path("detail/", AccountDetailView.as_view(), name="detail-account"),
    path("update/", AccountUpdateView.as_view(), name="update-account"),
    path("change-password/", ChangePasswordView.as_view(), name="change-password"),
]
