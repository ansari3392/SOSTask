import jwt
from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers.verify_email import EmailVerificationSerializer
from utils.token import decode_temp_token

User = get_user_model()

class VerifyEmailAPIView(APIView):
    permission_classes = []

    def get(self, *args, **kwargs):
        serializer = EmailVerificationSerializer(data=self.request.data)
        serializer.is_valid()
        token: str = serializer.validated_data.get('token')
        try:
            payload: dict = decode_temp_token(token)
        except jwt.ExpiredSignatureError as e:
            raise ValidationError({'error': 'Activation Expired'})
        except jwt.exceptions.DecodeError as e:
            raise ValidationError({'error': 'Invalid token'})
        else:
            user = User.objects.filter(id=payload['user_id']).first()
            if not user:
                raise ValidationError({'error': 'User not found'})
            if user.is_active:
                raise ValidationError({'error': 'Your account is already activated'})
            user.activate()
            return Response({'message': 'Successfully activated'}, status=status.HTTP_200_OK)









