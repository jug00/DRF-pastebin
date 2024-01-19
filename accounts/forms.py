from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User


# Форма для создания пользователя, наследующаяся от UserCreationForm
class CustomUserCreationForm(UserCreationForm):
    # Добавление дополнительного поля email типа EmailField
    email = forms.EmailField()

    class Meta:
        # Указание модели User и полей, включая те, которые предоставляет UserCreationForm
        model = User
        fields = UserCreationForm.Meta.fields


# Форма для изменения пользователя, наследующаяся от UserChangeForm
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        # Указание модели User и полей, включая те, которые предоставляет UserChangeForm
        model = User
        fields = UserChangeForm.Meta.fields
