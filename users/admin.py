from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users


@admin.register(Users)
class CustomUserAdmin(UserAdmin):
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("phone_number", "avatar", "city")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("email", "phone_number", "password1", "password2"),
            },
        ),
    )
    list_display = ("email", "phone_number", "is_staff")
    search_fields = ("email", "phone_number")
    ordering = ("email",)