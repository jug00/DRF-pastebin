from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView
import debug_toolbar


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("snippets.urls")),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/auth/", include('accounts.urls')),
    path('__debug__/', include(debug_toolbar.urls)),
]
