from rest_framework import permissions


# Пользовательское разрешение для проверки владельца или разрешенных методов
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Разрешено безопасные методы (например, GET)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Проверяем, является ли текущий пользователь владельцем объекта
        return obj.owner == request.user
