from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Account
from .serializers import (
    AccountSerializer,
    ChangePasswordSerializer,
    CreateAccountSerializer,
    UpdateAccountSerializer,
)


class AccountCreateView(generics.CreateAPIView):
    """Allow to user to create a new account"""

    queryset = Account.objects.all()
    serializer_class = CreateAccountSerializer
    permission_classes = [AllowAny]
    authentication_classes = []


class AccountDetailView(generics.RetrieveAPIView):
    """allow to User to see a lot of detail"""

    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    # without lookup feilds
    def get_object(self):
        return self.request.user


class AccountUpdateView(generics.UpdateAPIView):
    """Update User Information"""

    queryset = Account.objects.all()
    serializer_class = UpdateAccountSerializer

    def get_object(self):
        return self.request.user


class ChangePasswordView(APIView):
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)
        user = request.user

        if serializer.is_valid():
            if not user.check_password(serializer.validated_data["old_password"]):
                return Response(
                    {"old_password": ["Wrong password."]},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user.set_password(serializer.validated_data["new_password"])
            user.save()
            return Response(
                {"detail": "Password updated successfully."}, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
