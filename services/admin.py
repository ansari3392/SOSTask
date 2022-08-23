from django.contrib import admin
from django.core.exceptions import ValidationError

from services.models import RequestService
from services.models.service import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('name', 'price',)


@admin.register(RequestService)
class RequestServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'user', 'is_confirmed', 'service')
    list_filter = ('state', 'user', 'is_confirmed', 'service')

    def get_queryset(self, request):
        queryset = RequestService.objects.exclude(state=RequestService.StateChoices.CREATED)
        return queryset

