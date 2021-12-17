from django.db import models
from film.models import Film

class Fact(models.Model):
    text = models.CharField(max_length=1500)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='facts')
