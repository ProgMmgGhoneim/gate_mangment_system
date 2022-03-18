from rest_framework import serializers

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=120, allow_blank=False, required=True)
    password = serializers.CharField(style={'input_type': 'password'}, required=True)