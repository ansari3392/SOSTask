from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import UpdateAPIView, get_object_or_404, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from services.api.serializers.service_request import RequestServiceCreateSerializer, RequestServiceConfirmSerializer, \
    RequestServiceUpdateRetrieveSerializer
from services.models import RequestService


class RequestServiceCreateAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        serializer = RequestServiceCreateSerializer(
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


class RequestServiceDetailAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RequestServiceUpdateRetrieveSerializer

    def get_queryset(self):
        queryset = RequestService.objects.filter(user=self.request.user)
        return queryset


class RequestServiceUpdateAPIView(UpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = RequestServiceUpdateRetrieveSerializer

    def get_queryset(self):
        queryset = RequestService.objects.filter(user=self.request.user)
        return queryset

    def get_object(self):
        queryset = self.get_queryset()
        pk = self.kwargs.get('pk')
        obj: RequestService = get_object_or_404(queryset, pk=pk)
        if obj.is_confirmed:
            raise ValidationError({'message': 'You cannot edit confirmed requests'})
        return obj


class ConfirmRequestServiceAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, *args, **kwargs):
        serializer = RequestServiceConfirmSerializer(
            data=self.request.data,
            context={'request': self.request}
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
