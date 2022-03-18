import email
from email.policy import default

from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from django.contrib.auth.models import User

from staff.models.staff import Staff
from staff.serializer.user_serializer import UserSerializer


class StaffSerializer(serializers.Serializer):
    username = serializers.CharField(
        max_length=120, allow_blank=False, required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(
        style={'input_type': 'password'}, required=True)
    email = serializers.CharField(max_length=120, required=False)
    gate_ids = serializers.ListField(child=serializers.CharField(required=False))
    is_active = serializers.NullBooleanField(required=False, default=False)
    is_admin = serializers.NullBooleanField(required=False)
    is_operation = serializers.NullBooleanField(required=False)
    is_supervisor = serializers.NullBooleanField(required=False)
    tabs = serializers.JSONField(required=False)

    def create(self, validated_data):
        user = User(username=validated_data.get('username'), 
                    password=validated_data.get('password'),
                    email=validated_data.get('email')
                    )
        user.save()
        staff = Staff(
            user=user,
            is_active=validated_data.get('is_active'),
            tabs=validated_data.get('tabs'),
            is_admin=validated_data.get('is_admin'),
            is_operation=validated_data.get('is_operation'),
            is_supervisor=validated_data.get('is_supervisor')
        )
        staff.save()
        staff.gate.add(*validated_data.get('gate_ids'))
        return staff

    def update(self, staff, validated_data):
        user = staff.user
        user.username = validated_data.get('username')
        user.password = validated_data.get('password')
        user.save()
        
        staff.gate.add(*validated_data.get('gate_ids'))
        staff.is_active=validated_data.get('is_active')
        staff.tabs=validated_data.get('tabs')
        staff.is_admin=validated_data.get('is_admin')
        staff.is_operation=validated_data.get('is_operation')
        staff.is_supervisor=validated_data.get('is_supervisor')
        staff.save()
        return staff

class StaffModelSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Staff
        fields = '__all__'
