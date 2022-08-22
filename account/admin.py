from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import UserType
from account.models.user import CustomUser


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percent',)
    list_filter = ('name', 'percent',)


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ('id', 'username', 'is_superuser')
    list_filter = ('username', 'user_type')

