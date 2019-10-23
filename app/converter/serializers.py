from rest_framework import serializers
from .models import Currencies, Rates


class CurrenciesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Currencies
        fields = ['code', 'name']


class RatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rates
        fields = ['created', 'base', 'curr', 'value']


class ConvertSerializer(serializers.Serializer):
    result = serializers.FloatField()
    code = serializers.CharField()
