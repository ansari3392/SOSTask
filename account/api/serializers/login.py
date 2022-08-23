from django.contrib.auth import get_user_model
from django.contrib.auth.models import update_last_login
from rest_framework import serializers
from rest_framework.exceptions import AuthenticationFailed
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class ObtainAccessTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=255,
        min_length=3
    )
    password = serializers.CharField(
        max_length=68,
        min_length=6,
        write_only=True
    )

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs: dict):
        email = attrs.get('email')
        password = attrs.get('password')
        user: User = User.objects.filter(email=email).first()
        if not user:
            raise AuthenticationFailed('Your email or password is wrong')
        if not user.is_active:
            raise AuthenticationFailed('your account is not active')
        if not user.check_password(password):
            raise AuthenticationFailed('Your email or password is wrong')
        refresh = self.get_token(user)
        data = {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }

        update_last_login(None, user)

        return data
