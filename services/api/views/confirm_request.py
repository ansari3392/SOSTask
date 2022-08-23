from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from services.api.serializers.confirm_requrest import ConfirmRequestSerializer
from services.models import RequestService


class ConfirmRequestAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        serializer = ConfirmRequestSerializer(
            data=self.request.data,
            )
        serializer.is_valid(raise_exception=True)
        request_service: RequestService = serializer.validated_data.get('request_service')
        request_service.confirm_request()

        status_code = status.HTTP_200_OK
        response = {
            'message': 'confirmed successfully',
            'payment_url': 'https://google.com'
        }

        return Response(
            data=response,
            status=status_code
        )
