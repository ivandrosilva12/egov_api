from rest_framework import serializers

from .models import Category, Imovel, ImovelWorkers, Room, RoomImage, RoomType


class RoomTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomType
        fields = ['name']


class RoomCategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']


class ImovelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Imovel
        fields = '__all__'


class RoomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Room
        fields = '__all__'


class RoomImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = RoomImage
        fields = '__all__'


class ImovelWorkersSerializer(serializers.ModelSerializer):

    class Meta:
        model = ImovelWorkers
        fields = '__all__'
