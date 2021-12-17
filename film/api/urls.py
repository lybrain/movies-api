from rest_framework import routers
from film.api.views import FilmViewSet

film_router = routers.DefaultRouter()
film_router.register('film', FilmViewSet, basename='Film')