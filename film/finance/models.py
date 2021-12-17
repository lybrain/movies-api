from django.db import models

# Create your models here.
class Finance(models.Model):
    budget = models.DecimalField(decimal_places=2, max_digits=10)