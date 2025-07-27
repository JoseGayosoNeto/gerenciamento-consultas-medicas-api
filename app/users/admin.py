from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser

    list_display = ("email", "username", "uuid_id", "is_staff", "is_active")
    search_fields = ("email", "username", "uuid_id")
    ordering = ("email",)
    fieldsets = (
        (None, {
            "fields": ("email", "username", "uuid_id", "password")
        }),
        (
            "Permissions", {
                "fields": ("is_staff", "is_active", "is_superuser", "groups", "user_permissions")
            }
        ),
        ("Important dates", {
            "fields": ("last_login", "date_joined")
        }),
    )
    add_fieldsets = ((
        None,
        {
            "classes": ("wide",),
            "fields": (
                "email", "username", "password1", "password2", "is_staff", "is_active", "groups",
                "user_permissions"
            ),
        },
    ),)

    readonly_fields = ("uuid_id",)  # para que não possa ser editado manualmente
