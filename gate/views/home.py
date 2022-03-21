from rest_framework import viewsets, status
from rest_framework.response import Response

from gate_mangment_system.authonticaton.api_authontication import APIAuthentication
from staff.models.visitor import Visitor
from staff.models.car import Car
from staff.models.staff import Staff
from gate.models.camera import Camera
from gate.models.gate import Gate

class HomeViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    authentication_classes = [APIAuthentication, ]
    
    def create(self, request):
        response = {
            "camera": Camera.objects.count(),
            "visitor":Visitor.objects.count(),
            "gate": Gate.objects.count(),
            "car":Car.objects.count(),
            "staff":Staff.objects.count(),
            "reports": 5
        }
        
        return Response(data=response, 
                        status=status.HTTP_200_OK)