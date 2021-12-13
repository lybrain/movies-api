from django.utils.translation import activate
from rest_framework import serializers
from film.models import Film
from country.api.serializers import CountrySerializer
from genre.api.serializers import GenreSerializer
from country.models import Country
from django.core.exceptions import ObjectDoesNotExist
from person.api.serializers import PersonSerializer
from person.models import Person
from django.db import transaction

class FilmSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    director = PersonSerializer()

    @transaction.atomic
    def create(self, validated_data):
        countries = validated_data.pop('country', None)
        genries = validated_data.pop('genre', None)
        director = validated_data.pop('director', None)
        if director:
            director_obj = Person.objects.create(first_name=director['first_name'])
            validated_data['director'] = director_obj
        film = super().create(validated_data)
        # many to many
        
        for country in countries:
            try:
                country_obj = Country.objects.get(title=country['title'])
            except ObjectDoesNotExist:
                country_obj = Country.objects.create(title=country['title'])
            film.country.add(country_obj)
        # students add genre
        # raise ObjectDoesNotExist 
        return film
        
        

    class Meta:
        model = Film
        fields = '__all__'