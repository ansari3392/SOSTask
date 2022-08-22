from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        allow_blank=False,
        allow_null=False
    )
    password2 = serializers.CharField(
        write_only=True,
        required=True,
        allow_blank=False,
        allow_null=False
    )
    old_password = serializers.CharField(
        write_only=True,
        required=True,
        allow_blank=False,
        allow_null=False
    )

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError({"old_password": "Old password is not correct"})
        return value
