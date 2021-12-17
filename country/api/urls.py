from rest_framework import routers
from country.api.views import CountryViewSet

country_router = routers.DefaultRouter()
country_router.register('country', CountryViewSet, basename='Country')