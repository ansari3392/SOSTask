from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(
        max_length=150,
        required=True,
        allow_blank=False,
        allow_null=False,
    )
    password = serializers.CharField(
        max_length=150,
        write_only=True,
        required=True,
        validators=[validate_password]
    )
    password2 = serializers.CharField(
        max_length=150,
        write_only=True,
        required=True
    )

    @staticmethod
    def validate_email(value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                {"username": "try another email"}
            )
        return value

    def validate(self, attrs: dict) -> dict:
        if attrs.get('password') != attrs.get('password2'):
            raise serializers.ValidationError(
                {"password": "Passwords do not match"}
            )
        return attrs

    def create(self, validated_data: dict) -> User:
        user = User.objects.create_user(
            email=validated_data.get('email'),
            password=validated_data.get('password')
        )
        return user

    def update(self, instance, validated_data: dict) -> None:
        pass
