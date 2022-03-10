from crypt import methods
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action

from gate_mangment_system.authonticaton.api_authontication import APIAuthentication
from gate_mangment_system.pagination.standred_pagination import StandardResultsSetPagination
from gate.serializer.gate_serializer import GateSerializer
from gate.models.gate import Gate
from staff.models.staff import Staff

class GateViewSet(viewsets.ModelViewSet):
    
    authentication_classes = [APIAuthentication, ]
    pagination_class = StandardResultsSetPagination
    queryset = Gate.objects.all()
    serializer_class = GateSerializer

    def get_queryset(self, request):
        query_param = self.request.GET
        name = query_param.get('name')
        if name:
            gate = Gate.objects.filter(name=name)
            return self.queryset
        
        return self.queryset

    def create(self, request):
        if not self.request.user.has_perm('gate.can_add_gate'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        data = self.request.data
        serializer = GateSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(data={"message":"Gate Created Successfully"}, 
                        status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        try:
            gate = Gate.objects.get(id=pk)
        except:
            return Response(data={"message": " This Gate is not exsits"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=GateSerializer(gate).data,
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not self.request.user.has_perm('gate.can_update_gate'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            gate = Gate.objects.get(id=pk)
        except:
            return Response(data={"message": " This Gate is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = self.request.data
        serializer = GateSerializer(gate, data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data={"message":"Gate Updated Successfully"}, 
                        status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        if not self.request.user.has_perm('gate.can_delete_camera'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            gate = Gate.objects.get(id=pk)
        except:
            return Response(data={"message": " This Gate is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        gate.delete()
        return Response(data={"message": " This Gate Deleted"}, status=status.HTTP_200_OK)

    @action(detail=False, methods=['post'])
    def staff_gate(self, request):
        user = self.request.user
        staff = Staff.objects.filter(user=user, is_active=True).last()
        if not staff:
            return Response(data={"message": "This User have no gate"},
                            status=status.HTTP_400_BAD_REQUEST)
        return Response (GateSerializer(staff.gate, many=True).data, status=status.HTTP_200_OK)