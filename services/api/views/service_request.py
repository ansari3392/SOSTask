from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from services.api.serializers.service_request import ServiceRequestSerializer


class RequestServiceAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        serializer = ServiceRequestSerializer(
            data=self.request.data,
            context={'request': self.request}
        )
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(
            data={'message': 'request created successfully.'
                             'your request will be cancelled after one day,'
                             ' if you dont confirm your request.'},
            status=status.HTTP_201_CREATED
        )

