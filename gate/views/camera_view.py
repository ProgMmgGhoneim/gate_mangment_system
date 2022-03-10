from rest_framework import viewsets, status
from rest_framework.response import Response

from gate.models.camera import Camera
from gate.serializer.camera_serializer import CameraSerializer
from gate_mangment_system.authonticaton.api_authontication import APIAuthentication
from gate_mangment_system.pagination.standred_pagination import StandardResultsSetPagination

class CameraViewSet(viewsets.ModelViewSet):

    serializer_class = CameraSerializer
    authentication_classes = [APIAuthentication, ]
    pagination_class = StandardResultsSetPagination
    queryset = Camera.objects.all()

    def get_queryset(self):
        query_param = self.request.GET
        name = query_param.get('name')
        if name:
            camera = Camera.objects.filter(name=name)
            return self.queryset
        
        return self.queryset

    def create(self, request):
        if not self.request.user.has_perm('gate.can_add_camera'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        data = self.request.data
        serializer = CameraSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(data={"message":"Camera Created Successfully"}, 
                        status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            camera = Camera.objects.get(id=pk)
        except:
            return Response(data={"message": " This Camera is not exsits"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=CameraSerializer(camera).data,
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not self.request.user.has_perm('gate.can_update_camera'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            camera = Camera.objects.get(id=pk)
        except:
            return Response(data={"message": " This Camera is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = self.request.data
        serializer = CameraSerializer(camera, data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data={"message":"Camera Updated Successfully"}, 
                        status=status.HTTP_200_OK)
    
    def destroy(self, request, pk=None):
        if not self.request.user.has_perm('gate.can_delete_camera'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            camera = Camera.objects.get(id=pk)
        except:
            return Response(data={"message": " This Camera is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        camera.delete()
        return Response(data={"message": " This Camera Deleted"}, status=status.HTTP_200_OK)
