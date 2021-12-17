from django.db import models
from film.models import Film

# Create your models here.
class Review(models.Model):
    text = models.CharField(max_length=3000)
    created_date = models.DateTimeField(auto_now_add=True)
    film = models.ForeignKey(Film, on_delete=models.CASCADE, related_name='reviews')