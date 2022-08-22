from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from account.api.serializers.register import RegisterSerializer

User = get_user_model()


class RegisterAPIView(CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        user.send_activation_link()
        return Response({'message': 'We have sent you a link to activate your account'}, status=status.HTTP_201_CREATED)
