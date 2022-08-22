from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers.change_password import ChangePasswordSerializer

User = get_user_model()


class ChangePasswordView(APIView):
    permission_classes = (IsAuthenticated,)

    def put(self, *args, **kwargs):
        serializer = ChangePasswordSerializer(
            data=self.request.data,
            context={'request': self.request}
        )
        user = self.request.user
        serializer.is_valid(raise_exception=True)
        password = serializer.validated_data.get('password')
        user.set_password(password)
        user.save()

        return Response(
            data={'message': 'Password changed successfully'},
            status=status.HTTP_200_OK
        )
