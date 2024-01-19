from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _


# Класс CustomUserManager, который расширяет базовый UserManager Django
class CustomUserManager(UserManager):
    # Метод для создания обычного пользователя
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email=email, password=password, **extra_fields)

    # Метод для создания суперпользователя
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")

        return self._create_user(email=email, password=password, **extra_fields)


# Класс User, который наследуется от AbstractUser и использует CustomUserManager
class User(AbstractUser):
    # Убираем поля имени, фамилии из модели
    first_name = None
    last_name = None

    # Использование email в качестве уникального идентификатора пользователя
    email = models.EmailField(_("email address"), unique=True)
    # Использование email в качестве поля для входа
    USERNAME_FIELD = "email"
    # Список дополнительных полей, которые требуется заполнять при создании пользователя
    REQUIRED_FIELDS = ["username"]
    # Использование CustomUserManager для управления объектами пользователя
    objects = CustomUserManager()

    class Meta:
        # Указание порядка сортировки по умолчанию
        ordering = ["-id"]
