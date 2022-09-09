from django.urls import include, path
from rest_framework import routers

from .apis import CountryViewSet, PollutantViewSet, country, country_detail


router = routers.DefaultRouter()
router.register('pollutant', PollutantViewSet)
router.register('country', CountryViewSet)

# examples
# http://127.0.0.1:8000/api/airpollution/
# http://127.0.0.1:8000/api/airpollution/pollutant/
urlpatterns = [
    path('', include(router.urls)),
    path('v2/country/', country),
    path('v2/country/<str:pk>/', country_detail),
]
