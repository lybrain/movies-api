from django.core.management.base import BaseCommand
from film.models import Film

# class Command(BaseCommand):
#     def handle(self, **options):
queryset = Film.objects.select_related(
    "finance").filter(id__in=[25, 26, 27]).all()
films = []
for film in queryset:
    films.append({"name": film.title, "budget": film.finance.budget})

print(films)
