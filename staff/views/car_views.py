from rest_framework.decorators import api_view, authentication_classes, parser_classes
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from gate_mangment_system.authonticaton.api_authontication import APIAuthentication
from gate_mangment_system.pagination.standred_pagination import StandardResultsSetPagination
from staff.serializer.car_serializer import CarSerializer
from staff.models.car import Car


class CarViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = [APIAuthentication, ]
        
    def get_queryset(self):
        query_param = self.request.GET
        return self.queryset
    
    def retrieve(self, request, pk=None):
        try:
            car = Car.objects.get(id=pk)
        except:
            return Response(data={"message": " This Car is not exsits"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=CarSerializer(car).data,
                        status=status.HTTP_200_OK)
    
    def create(self, request):
        if not self.request.user.has_perm('staff.can_add_car'):
            return Response(data={"message": "Permission Denied"}, 
                        status=status.HTTP_403_FORBIDDEN)
        data = self.request.data
        serializer = CarSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(data={"message":"Car Created Successfully"}, 
                        status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        try:
            car = Car.objects.get(id=pk)
        except:
            return Response(data={"message": " This Car is not exsits"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=CarSerializer(car).data,
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not self.request.user.has_perm('staff.can_update_car'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            car = Car.objects.get(id=pk)
        except:
            return Response(data={"message": " This Car is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = self.request.data
        serializer = CarSerializer(car, data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data={"message":"Car Updated Successfully"}, 
                        status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        if not self.request.user.has_perm('staff.can_destroy_car'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            car = Car.objects.get(id=pk)
        except:
            return Response(data={"message": " This Car is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        car.delete()
        return Response(data={"message": " This Car Deleted"}, status=status.HTTP_200_OK)
