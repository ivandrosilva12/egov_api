from rest_framework import serializers
from .models import Province, County


class ProvinceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Province
        fields = ['name']


class CountySerializer(serializers.ModelSerializer):

    class Meta:
        model = County
        fields = '__all__'
