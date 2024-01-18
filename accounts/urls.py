from django.urls import path, include
from . import views
from dj_rest_auth.views import PasswordResetConfirmView

urlpatterns = [
    path(
        "password/reset/confirm/<str:uidb64>/<str:token>",
        PasswordResetConfirmView.as_view(),
        name="password_reset_confirm",
    ),
    path("", include("dj_rest_auth.urls")),
    path(
        "registration/account-confirm-email/<str:key>/", views.ConfirmEmailView.as_view(), name="account_confirm_email"
    ),
    path("registration/", include("dj_rest_auth.registration.urls")),
]
