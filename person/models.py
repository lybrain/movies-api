from django.db import models

class Person(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    middle_name = models.CharField(max_length=300, null=True)