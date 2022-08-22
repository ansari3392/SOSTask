from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from account.api.serializers.login import LoginSerializer


class LoginAPIView(APIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'message': '...'}, status=status.HTTP_200_OK)
