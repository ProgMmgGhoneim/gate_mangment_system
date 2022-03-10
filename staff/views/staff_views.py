from itertools import count
from re import I
from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

from staff.models.staff import Staff
from staff.serializer.staff_serializer import StaffSerializer, StaffModelSerializer, StaffFilterSerializer

from gate.models.gate import Gate


class StaffViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer
    pagination_class = LimitOffsetPagination
    # authentication_classes = [SessionAuthentication, BasicAuthentication]
    # permission_classes = [IsAuthenticated]

    def create(self, request):
        """
            Create USer
            Create Staff
        """
        # Check Request body
        serializer = StaffSerializer(data=self.request.data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        # Check Gate
        gate = serializer.validated_data.pop('gates')
        gate = Gate.objects.filter(id__in=gate)
        if not gate:
            return Response(data={"message": "Please Enter A valid Data"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create user
        username = serializer.validated_data.pop('username')
        password = serializer.validated_data.pop('password')
        email = serializer.validated_data.pop('email')
        user, created = User.objects.get_or_create(username=username, password=password, email=email)
        if not created:
            return Response(data={"message": "The username already exsits"}, status=status.HTTP_400_BAD_REQUEST)
            
        # Create Staff
        staff = Staff.objects.create(user=user,
                                     **serializer.validated_data)
        staff.gate.add(*gate)
        return Response(data={"message":"Staff Created successfully", "data": StaffModelSerializer(staff).data}, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        try:
            staff = Staff.objects.get(id=pk)
        except:
            return Response(data={"message": "This Staff is not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        return Response(data={"message": "This Staff is not exist"}, status=status.HTTP_400_BAD_REQUEST)

        # 
        
    @action(detail=False, methods=['get'])
    def get_query(self, request):
        """
            Get spesific data
        """
        data = self.request.GET
        if not data:
            return Response(data=StaffModelSerializer(self.queryset, many=True).data, status=status.HTTP_200_OK)
            
        serializer = StaffFilterSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        staff = Staff.objects.filter(**serializer.validated_data)
        
        return Response(data=StaffModelSerializer(staff,many=True).data, status=status.HTTP_200_OK)

    @action(detail=True, methods=['post'])
    def deactive(self, request, pk=None):
        try:
            staff = Staff.objects.get(id=pk)
        except:
            return Response(data={"message": "This Staff is not exist"}, status=status.HTTP_400_BAD_REQUEST)
        
        if not staff.is_active:
            return Response(data={"message": "This user is already deactivated"}, status=status.HTTP_400_BAD_REQUEST)
        
        staff.is_active = False
        staff.save(update_fields=['is_active'])
        return Response(data={"message": "This user deactivated Successfully"}, status=status.HTTP_200_OK)

   