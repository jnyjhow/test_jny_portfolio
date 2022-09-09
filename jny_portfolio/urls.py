from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # incluindo projeto com react
    path('react/', include('frontend.urls')),
    path('admin/', admin.site.urls),
    path('', include('website.urls')),
    path('accounts/', include('accounts.urls')),
    path('airpollution/', include('airpollution.urls')),
    # incluindo ao projeto api com DRF
    path('api/airpollution/', include('airpollution.api_urls')),
    path('my_finances/', include('my_finances.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


