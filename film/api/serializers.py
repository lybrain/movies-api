from rest_framework import serializers
from film.models import Film
from country.api.serializers import CountrySerializer
from country.models import Country
from django.core.exceptions import ObjectDoesNotExist
from person.api.serializers import PersonSerializer
from django.db import transaction
from film.finance.models import Finance
from film.finance.api.serializers import FinanceSerializer
from film.fact.api.serializers import FactSerializer
from film.fact.models import Fact

class FilmSerializer(serializers.ModelSerializer):
    finance = FinanceSerializer()
    countries = CountrySerializer(many=True)
    facts = FactSerializer(many=True)

    @transaction.atomic
    def create(self, validated_data):
        countries = validated_data.pop('countries', None)
        finance = validated_data.pop('finance', None)
        facts = validated_data.pop('facts', None)
        film = super().create(validated_data)

        # one to one 
        if finance:
            finance_obj = Finance.objects.create(**finance)
            film.finance = finance_obj
            film.save()
        # one to many
        if facts:
            for fact in facts:
                fact['film'] = film
                Fact.objects.create(**fact)
        # many to many
        for country in countries:
            try:
                country_obj = Country.objects.get(title=country['title'])
            except ObjectDoesNotExist:
                country_obj = Country.objects.create(title=country['title'])
            film.countries.add(country_obj)
        film.save()
        
        # raise ObjectDoesNotExist # when you goes to @atomic
        return film
        
        

    class Meta:
        model = Film
        fields = '__all__'


class HelloWorldSerializer(serializers.Serializer):
    text = serializers.CharField()