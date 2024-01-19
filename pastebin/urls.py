from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
import debug_toolbar


urlpatterns = [
    # Административная панель Django
    path("admin/", admin.site.urls),
    # Включение URL-маршрутов из приложения "snippets"
    path("api/", include("snippets.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Swagger UI для просмотра схемы API
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    # URL-маршруты для аутентификации в API
    path("api/auth/", include("accounts.urls")),
    # URL-маршруты для панели отладки Django Debug Toolbar
    path("__debug__/", include(debug_toolbar.urls)),
]
