from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class ResetPasswordRequestSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        min_length=2
    )

    class Meta:
        model = User
        fields = ('email',)
