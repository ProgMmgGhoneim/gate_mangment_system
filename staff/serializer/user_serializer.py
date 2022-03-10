from rest_framework import serializers


class UserSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=200, required=True)
    id = serializers.IntegerField(required=True)