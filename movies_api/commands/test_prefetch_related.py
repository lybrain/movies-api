from django.core.management.base import BaseCommand
from film.models import Film

# class Command(BaseCommand):
#     def handle(self, **options):
queryset = Film.objects.select_related("finance").prefetch_related("countries").filter(id__in=[25, 26, 27]).all()
films = []
for film in queryset:
    film_data = {"name": film.title,"budget": film.finance.budget, "countries": []}
    for country in film.countries.all():
        film_data["countries"].append(country.title)
        films.append(film_data)

print(films)
