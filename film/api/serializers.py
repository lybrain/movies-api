from django.utils.translation import activate
from rest_framework import serializers
from film.models import Film
from country.api.serializers import CountrySerializer
from genre.api.serializers import GenreSerializer
from country.models import Country
from django.core.exceptions import ObjectDoesNotExist
from human.api.serializers import HumanSerializer
from human.models import Human

class FilmSerializer(serializers.ModelSerializer):
    country = CountrySerializer(many=True)
    genre = GenreSerializer(many=True)
    director = HumanSerializer()

    def create(self, validated_data):
        countries = validated_data.pop('country', None)
        genries = validated_data.pop('genre', None)
        director = validated_data.pop('director', None)
        if director:
            director_obj = Human.objects.create(first_name=director['first_name'])
            validated_data['director'] = director_obj
        film = super().create(validated_data)
        return film


        # countries_to_add = []
        # for country in countries:
        #     try:
        #         country_obj = Country.objects.get(title=country['title'])
        #     except:
        #         country_obj = Country.objects.create(title=country['title'])
        #     countries_to_add.append(country_obj.id)
        # new_countries = Country.objects.filter(id__contains=countries_to_add)
        # film.country.add(new_countries)
        # film.save()
        
        

    class Meta:
        model = Film
        fields = '__all__'