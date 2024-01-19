from django.urls import path, include
from . import views
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    # URL для подтверждения сброса пароля с использованием токена и uidb64
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    # Включение URL-маршрутов для аутентификации и регистрации из dj_rest_auth
    path("", include("dj_rest_auth.urls")),
    # URL для подтверждения адреса электронной почты при регистрации
    path(
        "registration/account-confirm-email/<str:key>/", views.ConfirmEmailView.as_view(), name="account_confirm_email"
    ),
    # Включение URL-маршрутов для регистрации из dj_rest_auth.registration
    path("registration/", include("dj_rest_auth.registration.urls")),
]
