from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAdminUser

from services.api.serializers.service_request import RequestServiceUpdateRetrieveSerializer
from services.models import RequestService


class GetUserRequestsAPIView(ListAPIView):
    permission_classes = [IsAdminUser, ]
    serializer_class = RequestServiceUpdateRetrieveSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            queryset = RequestService.objects.filter(user_id=user_id)
        else:
            raise ValidationError({'message': 'you didnt send user id'})
        return queryset
