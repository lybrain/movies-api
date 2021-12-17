from rest_framework import serializers
from film.finance.models import Finance

class FinanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Finance
        fields = '__all__'