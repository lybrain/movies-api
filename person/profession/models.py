from django.db import models

class Profession(models.Model):
    title = models.CharField(max_length=1000)

    def __str__(self) -> str:
        return self.title