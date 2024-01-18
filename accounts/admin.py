from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import gettext_lazy as _


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ("username", "email", "is_staff")
    fieldsets = (
        (None, {"fields": ("username", "email", "password")}),
        (
            _("Permissions"),
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
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2"],
            },
        ),
    ]
    search_fields = ("username", "email")
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm


admin.site.register(User, CustomUserAdmin)
