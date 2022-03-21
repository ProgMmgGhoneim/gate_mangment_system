from rest_framework import serializers

from gate.models.gate import Gate

class GateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gate
        fields = '__all__'