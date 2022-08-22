from django.contrib.auth import get_user_model
from rest_framework import serializers
User = get_user_model()


class EmailVerificationSerializer(serializers.ModelSerializer):
    token = serializers.CharField(max_length=555)

    class Meta:
        model = User
        fields = ['token']
