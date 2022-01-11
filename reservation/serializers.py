from rest_framework import serializers

from .models import CheckIn, CheckOut, Reservation


class ReservationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Reservation
        fields = '__all__'


class CheckInSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckIn
        fields = '__all__'


class CheckOutSerializer(serializers.ModelSerializer):

    class Meta:
        model = CheckOut
        fields = '__all__'
