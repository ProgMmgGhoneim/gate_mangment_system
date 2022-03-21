from dataclasses import field
from rest_framework import serializers

from staff.models.visitor import Visitor

class VisitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visitor
        fields = '__all__'