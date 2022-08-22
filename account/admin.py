from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from account.models import UserType
from account.models.user import CustomUser


@admin.register(UserType)
class UserTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'percent', 'is_default')
    list_filter = ('name', 'percent',)


@admin.register(CustomUser)
class UserAdmin(UserAdmin):
    list_display = ('id', 'email', 'user_type', 'is_active', 'is_superuser')
    list_filter = ('email', 'user_type', 'is_active',)
    ordering = ('email',)
    fieldsets = (
        (None, {"fields": ("password",)}),
        ("Personal info", {"fields": ("first_name", "last_name", "email", "user_type")}),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "password1", "password2"),
            },
        ),
    )
    search_fields = ("first_name", "last_name", "email")
