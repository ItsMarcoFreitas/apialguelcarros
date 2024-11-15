from rest_framework import serializers
from .models import CarRental

class CarRentalSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarRental
        fields = '__all__'