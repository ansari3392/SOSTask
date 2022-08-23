from django.contrib import admin

from services.models import RequestService
from services.models.service import Service

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price')
    list_filter = ('name', 'price',)


@admin.register(RequestService)
class RequestServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'state', 'user')
    list_filter = ('state', 'user')

