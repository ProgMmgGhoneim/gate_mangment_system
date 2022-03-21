from rest_framework.decorators import api_view, authentication_classes, parser_classes
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser, FormParser

from gate_mangment_system.authonticaton.api_authontication import APIAuthentication
from gate_mangment_system.pagination.standred_pagination import StandardResultsSetPagination
from staff.serializer.visitor_serilaizer import VisitorSerializer
from staff.models.visitor import Visitor


class VisitorViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Visitor.objects.all()
    serializer_class = VisitorSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = [APIAuthentication, ]
    
    def get_queryset(self):
        query_param = self.request.GET
        name = query_param.get('name')
        if name:
            queryset = Visitor.objects.filter(name=name)
            return queryset
        return self.queryset

    def create(self, request):
        if not self.request.user.has_perm('staff.can_add_visitor'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
            
        data = self.request.data
        serializer = VisitorSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        
        serializer.save()
        return Response(data={"message":"Visitor Created Successfully"}, 
                        status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, pk=None):
        try:
            visitor = Visitor.objects.get(id=pk)
        except:
            return Response(data={"message": " This Visitor is not exsits"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=VisitorSerializer(visitor).data,
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not self.request.user.has_perm('staff.can_update_visitor'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            visitor = Visitor.objects.get(id=pk)
        except:
            return Response(data={"message": " This Visitor is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        
        data = self.request.data
        serializer = VisitorSerializer(visitor, data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, 
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data={"message":"Visitor Updated Successfully"}, 
                        status=status.HTTP_200_OK)

    def destroy(self, request, pk=None):
        if not self.request.user.has_perm('staff.can_delete_visitor'):
            return Response(data={"message": "Permission Denied"}, 
                            status=status.HTTP_403_FORBIDDEN)
        try:
            visitor = Visitor.objects.get(id=pk)
        except:
            return Response(data={"message": " This Visitor is not exsits"}, status=status.HTTP_400_BAD_REQUEST)
        visitor.delete()
        return Response(data={"message": " This Visitor Deleted"}, status=status.HTTP_200_OK)

@api_view(['POST',])
@authentication_classes([APIAuthentication,])
@parser_classes([MultiPartParser, FormParser])
def create_visitor(request):
    if not request.user.has_perm('staff.can_add_visitor'):
        return Response(data={"message": "Permission Denied"}, 
                        status=status.HTTP_403_FORBIDDEN)
        
    data = request.data
    serializer = VisitorSerializer(data=data)
    if not serializer.is_valid():
        return Response(data={"message": serializer.errors}, 
                        status=status.HTTP_400_BAD_REQUEST)
    
    serializer.save()
    return Response(data={"message":"Visitor Created Successfully"}, 
                    status=status.HTTP_201_CREATED)
