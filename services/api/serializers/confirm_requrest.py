from django.shortcuts import get_object_or_404
from rest_framework import serializers

from services.models import RequestService


class ConfirmRequestSerializer(serializers.Serializer):
    request_service = serializers.CharField(allow_null=False, allow_blank=False, required=True)

    @staticmethod
    def validate_service_request(request_id):
        request_service = get_object_or_404(RequestService, id=request_id)  # user should send id of request
        return request_service

