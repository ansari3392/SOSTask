from django.contrib.auth import get_user_model
from rest_framework.views import APIView

from account.api.serializers.reset_password import ResetPasswordRequestSerializer, SetNewPasswordSerializer

User = get_user_model()

from rest_framework import status

from rest_framework.response import Response

from django.conf import settings
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes
from django.utils.http import urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from utils.send_mail import send_email


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
            return Response({'success': 'We have sent you a link to reset your password'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'Email not found'}, status=status.HTTP_400_BAD_REQUEST)


class PasswordTokenCheckAPIView(APIView):
    serializer_class = SetNewPasswordSerializer

    def get(self, *args, **kwargs):
        pass
