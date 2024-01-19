from django.urls import path, include
from .views import SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


# Создание экземпляра DefaultRouter для удобного создания URL-маршрутов
router = DefaultRouter()
# Регистрация "viewset" SnippetViewSet с использованием пути 'snippets' и базового имени 'snippet'
router.register(r"snippets", SnippetViewSet, basename="snippet")
# Регистрация "viewset" UserViewSet с использованием пути 'users' и базового имени 'user'
router.register(r"users", UserViewSet, basename="user")


# Определение маршрутов URL для приложения Django, включая зарегистрированные "viewset"
urlpatterns = [
    # Включение зарегистрированных URL-маршрутов из router.urls
    path("", include(router.urls)),
]
