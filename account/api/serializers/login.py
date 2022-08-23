from django.contrib import auth
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed

User = get_user_model()

# class LoginSerializer(serializers.Serializer):
#     email = serializers.EmailField(
#         max_length=255,
#         min_length=3
#     )
#     password = serializers.CharField(
#         max_length=68,
#         min_length=6,
#         write_only=True
#     )
#
#     def validate(self, attrs: dict):
#         email = attrs.get('email')
#         password = attrs.get('password')
#         user: User = User.objects.filter(email=email).first()
#         if user.exist():
#             if not user.is_active:
#                 raise AuthenticationFailed('your account is not active')
#             user = auth.authenticate(email=email, password=password)
#         else:
#             raise AuthenticationFailed('Invalid credentials, try again')



