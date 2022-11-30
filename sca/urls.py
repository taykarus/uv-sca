from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from aplic.urls import router


urlpatterns = [
    path('restrito/', admin.site.urls),
    path('', include('aplic.urls')),
    path('api/v1/', include(router.urls)),
    path('auth/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
