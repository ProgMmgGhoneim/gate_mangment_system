from django.contrib import admin

from gate.models.camera import Camera
from gate.models.gate import Gate

@admin.register(Camera)
class CameraAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'gate', 'description', 'created_at', 'updated_at')
    
@admin.register(Gate)
class GateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'created_at', 'updated_at')
