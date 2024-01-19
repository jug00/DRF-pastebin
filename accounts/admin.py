from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .forms import CustomUserChangeForm, CustomUserCreationForm
from django.utils.translation import gettext_lazy as _


# Кастомный класс администратора для модели User, наследующийся от UserAdmin
class CustomUserAdmin(UserAdmin):
    model = User
    # Отображаемые поля в списке пользователей в административной панели
    list_display = ("username", "email", "is_staff")
    # Настройки полей, отображаемых при просмотре пользователя
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
    # Настройки полей, отображаемых при создании пользователя
    add_fieldsets = [
        (
            None,
            {
                "classes": ["wide"],
                "fields": ["email", "username", "password1", "password2"],
            },
        ),
    ]
    # Поля, по которым можно осуществлять поиск в административной панели
    search_fields = ("username", "email")
    # Используемые формы для изменения и создания пользователя
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm


# Регистрация модели User с кастомным классом администратора
admin.site.register(User, CustomUserAdmin)
