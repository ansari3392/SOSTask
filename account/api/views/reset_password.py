from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers.reset_password import ResetPasswordRequestSerializer, SetNewPasswordSerializer, \
    PasswordTokenCheckSerializer

User = get_user_model()


class ResetPasswordRequestAPIView(APIView):
    def post(self, *args, **kwargs):
        serializer = ResetPasswordRequestSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)

        email = self.request.data.get('email')

        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            user.send_reset_password_link(self.request)
            return Response({'message': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordTokenCheckAPIView(APIView):
    def post(self, *args, **kwargs):
        serializer = PasswordTokenCheckSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'now you can change your password'}, status=status.HTTP_200_OK)


class SetNewPasswordAPIView(APIView):

    def post(self, *args, **kwargs):
        serializer = SetNewPasswordSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Password reset success'}, status=status.HTTP_200_OK)
