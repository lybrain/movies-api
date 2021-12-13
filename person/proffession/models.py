from django.db import models

class Proffession(models.Model):
    title = models.CharField(max_length=1000)