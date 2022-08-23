from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers.login import ObtainAccessTokenSerializer


class GetAccessTokenAPIView(APIView):
    serializer_class = ObtainAccessTokenSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
