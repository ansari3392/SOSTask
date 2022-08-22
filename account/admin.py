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
    list_display = ('id', 'email', 'is_superuser')
    list_filter = ('email', 'user_type')
    ordering = ('email', )

