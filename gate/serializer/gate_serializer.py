from rest_framework import serializers

from gate.models.gate import Gate
from gate.serializer.camera_serializer import CameraSerializer


class GateSerializer(serializers.ModelSerializer):
    camera = serializers.SerializerMethodField()

    class Meta:
        model = Gate
        fields = '__all__'

    def get_camera(self, obj):
        return CameraSerializer(obj.camera_set.all(), many=True).data
