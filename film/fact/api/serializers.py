from rest_framework import serializers
from film.fact.models import Fact
from film.models import Film

class FactSerializer(serializers.ModelSerializer):
    film = serializers.PrimaryKeyRelatedField(queryset=Film.objects.all(),required=False)
    class Meta:
        model = Fact
        fields = '__all__'