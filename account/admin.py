from django.contrib import admin

from account.models import UserType


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percent',)
    list_filter = ('name', 'percent',)

