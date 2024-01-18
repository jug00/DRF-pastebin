from django.urls import path, include
from .views import SnippetViewSet, UserViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, basename='snippet')
router.register(r'users', UserViewSet, basename='user')


urlpatterns = [
    path("", include(router.urls)),
]
