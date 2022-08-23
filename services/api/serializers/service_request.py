from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from services.models import RequestService


class RequestServiceCreateSerializer(ModelSerializer):  # user should send id of service
    request_total_price = SerializerMethodField()

    @staticmethod
    def get_request_total_price(obj: RequestService) -> int:
        return obj.get_service_request_price()

    @staticmethod
    def validate_photo(image):
        filesize = image.size
        if filesize > settings.MEGABYTE_LIMIT * 1024 * 1024:
            raise ValidationError(f"Max file size is {settings.MEGABYTE_LIMIT}MB")
        return image

    class Meta:
        model = RequestService
        fields = (
            'service',
            'user_extra_description',
            'photo',
            'request_total_price'
        )
        readline_only_fields = [
            'request_total_price'
        ]


class RequestServiceUpdateRetrieveSerializer(ModelSerializer):  # user should send id of request
    request_total_price = SerializerMethodField()
    service_name = SerializerMethodField()

    @staticmethod
    def get_request_total_price(obj: RequestService) -> int:
        return obj.get_service_request_price()

    @staticmethod
    def get_service_name(obj: RequestService) -> str:
        return obj.service.name

    class Meta:
        model = RequestService
        fields = (
            'id',
            'service',
            'state',
            'service_name',
            'user_extra_description',
            'staff_extra_description',
            'photo',
            'is_confirmed',
            'request_total_price'
        )
        read_only_fields = [
            'id',
            'service_name',
            'request_total_price',
            'staff_extra_description',
            'state',
            'is_confirmed',
        ]


class RequestServiceConfirmSerializer(serializers.Serializer):  # user should send id of request
    request_service = serializers.IntegerField(
        required=True,
        allow_null=False,
    )

    def validate_request_service(self, request_id: int) -> RequestService:
        request_service = get_object_or_404(
            RequestService,
            id=request_id,
            user=self.context['request'].user
        )
        if request_service.is_confirmed:
            raise ValidationError({'message': 'Your request is already confirmed'})
        return request_service


