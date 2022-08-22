from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.auth import get_user_model
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from utils.send_mail import send_email

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
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=self.request).domain
            message = 'Hello, \n Use link below to reset your password  \n' + \
                      'http://' + current_site + reverse(
                'account:api:password_reset_confirm', kwargs={'uidb64': uidb64, 'token': token})

            send_email({
                'subject': 'Reset your password',
                'message': message,
                'from_email': settings.EMAIL_HOST_USER,
                'to_email': email
            })
            return Response({'message': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({'message': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordTokenCheckAPIView(APIView):
    def get(self, *args, **kwargs):
        serializer = PasswordTokenCheckSerializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'now you can change your password'}, status=status.HTTP_200_OK)


class SetNewPasswordAPIView(APIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': 'Password reset success'}, status=status.HTTP_200_OK)
