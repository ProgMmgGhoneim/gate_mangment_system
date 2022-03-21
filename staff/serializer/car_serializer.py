from rest_framework import serializers

from staff.models.car import Car

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'