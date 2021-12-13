from django.db import models
from country.models import Country
from genre.models import Genre
from person.models import Person

def film_directory_path(instance, filename):
    return 'film/{0}/{1}'.format(instance.title, filename)

class Film(models.Model):
    title = models.CharField(max_length=1000)
    production_year = models.DateField()
    preview_picture = models.ImageField(upload_to=film_directory_path, null=True)
    slogan = models.CharField(max_length=200)
    duration = models.PositiveSmallIntegerField()
    country = models.ManyToManyField(Country, related_name='films')
    genre = models.ManyToManyField(Genre, related_name='films')
    actors = models.ManyToManyField(Person, on_delete=models.SET_NULL, null=True, related_name="films")

