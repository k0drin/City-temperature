from rest_framework import serializers
from .models import City, CityTemperature

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['id', 'name', 'description']


class TemperatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityTemperature
        fields = ['value']