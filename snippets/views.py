from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import renderers
from rest_framework import viewsets
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page


from snippets.models import Snippet
from snippets.permissions import IsOwnerOrReadOnly
from snippets.serializers import SnippetSerializer
from accounts.serializers import UserSerializer
from .tasks import increment_views


# Определение ViewSet для сущности Snippet
class SnippetViewSet(viewsets.ModelViewSet):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    # Декоратор для создания дополнительного действия (action) для выделения синтаксиса в сниппете
    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    # Декоратор для добавления кэширования на уровне представления для действия "top"
    @method_decorator(cache_page(60 * 5))
    @action(detail=False)
    def top(self, request, *args, **kwargs):
        queryset = self.filter_queryset(Snippet.objects.all().order_by("-views"))

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    # Метод для сохранения владельца сниппета при его создании
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    # Метод для извлечения сниппета и инкрементации счетчика просмотров при его получении
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        increment_views.delay(instance.id)
        return Response(serializer.data)


# Определение ViewSet для сущности User
class UserViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
