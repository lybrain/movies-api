from django.db.models import fields
from rest_framework import serializers
from human.models import Human

class HumanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Human
        fields = '__all__'