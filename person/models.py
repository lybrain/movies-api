from django.db import models
from person.profession.models import Profession

class Person(models.Model):
    first_name = models.CharField(max_length=300)
    last_name = models.CharField(max_length=300)
    middle_name = models.CharField(max_length=300, null=True, blank=True)
    professions = models.ManyToManyField(Profession, related_name='persons')

    def __str__(self) -> str:
        return "{0} {1} {2}".format(self.middle_name,self.first_name,self.last_name)