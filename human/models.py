from django.db import models

class Human(models.Model):
    first_name = models.CharField(max_length=300)