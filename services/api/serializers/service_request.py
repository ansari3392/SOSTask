import datetime

from django.conf import settings
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from services.models import RequestService, Service


class ServiceRequestSerializer(ModelSerializer):
    service = serializers.CharField(allow_null=False, allow_blank=False, required=True)
    service_price = SerializerMethodField()
    service_name = SerializerMethodField()

    @staticmethod
    def get_service_price(obj: RequestService) -> int:
        return obj.get_service_request_price()

    @staticmethod
    def get_service_name(obj: RequestService) -> str:
        return obj.service.name

    @staticmethod
    def get_service(obj: RequestService) -> str:
        return obj.service.name

    @staticmethod
    def validate_photo(image):
        filesize = image.size
        if filesize > settings.MEGABYTE_LIMIT * 1024 * 1024:
            raise ValidationError(f"Max file size is {settings.MEGABYTE_LIMIT}MB")
        return image

    @staticmethod
    def validate_service(service_id):
        service = get_object_or_404(Service, id=service_id)  # user should send id of service
        return service

    # def validate(self, attrs: dict):
    #     service_id = attrs.get('service.id')
    #     user = self.context['request'].user
    #     if RequestService.objects.filter(
    #             user=user,
    #             service__id=service_id,
    #             confirmed_at__day=datetime.date
    #     ).exists():
    #         raise ValidationError('......')
    #
    #     return attrs

    class Meta:
        model = RequestService
        fields = (
            'service',
            'service_name',
            'user_extra_description',
            'photo',
            'service_price'
        )
