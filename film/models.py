from django.db import models
from country.models import Country
from genre.models import Genre
from person.models import Person
from film.finance.models import Finance

def film_directory_path(instance, filename):
    return 'film/{0}/{1}'.format(instance.title, filename)

class Film(models.Model):
    title = models.CharField(max_length=1000)
    production_year = models.DateField()
    preview_picture = models.ImageField(upload_to=film_directory_path, null=True)
    slogan = models.CharField(max_length=200)
    duration = models.PositiveSmallIntegerField()
    countries = models.ManyToManyField(Country, related_name='films')
    finance = models.OneToOneField(Finance, on_delete=models.CASCADE,null=True, related_name='film')
    # genre = models.ManyToManyField(Genre, related_name='films')
    # actors = models.ManyToManyField(Person, related_name="films")

