from email.policy import default
from rest_framework import serializers

from staff.models.staff import Staff
from staff.serializer.user_serializer import UserSerializer

from gate.models.gate import Gate
from gate.serializer.gate_serializer import GateSerializer

class StaffSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120, allow_blank=False, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, required=True)
    email = serializers.CharField(max_length=120, required=False)
    gates = serializers.ListField(child=serializers.CharField(required=False))
    is_active = serializers.NullBooleanField(required=False, default=False)
    is_admin = serializers.NullBooleanField(required=False)
    is_operation = serializers.NullBooleanField(required=False)
    is_supervisor = serializers.NullBooleanField(required=False)
    
class StaffModelSerializer(serializers.ModelSerializer):
    gate = GateSerializer()
    user = UserSerializer()
    
    class Meta:
        model = Staff
        fields = '__all__'
    
class StaffFilterSerializer(serializers.Serializer):
    user__username = serializers.CharField(max_length=120, required=False)
    id = serializers.IntegerField(required=False)
    is_active = serializers.NullBooleanField(required=False)
    is_admin = serializers.NullBooleanField(required=False)
    is_operation = serializers.NullBooleanField(required=False)
    is_supervisor = serializers.NullBooleanField(required=False)