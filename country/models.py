from django.db import models

class Country(models.Model):
    title = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.title