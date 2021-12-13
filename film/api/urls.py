from rest_framework import routers
from film.api.views import FilmCreateListView

film_router = routers.DefaultRouter()
film_router.register('film', FilmCreateListView, basename='Film')