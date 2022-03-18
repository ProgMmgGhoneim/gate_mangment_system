from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import LimitOffsetPagination

from gate_mangment_system.authonticaton.api_authontication import APIAuthentication

from staff.models.staff import Staff
from staff.serializer.staff_serializer import StaffSerializer, StaffModelSerializer

from gate.models.gate import Gate

from gate_mangment_system.pagination.standred_pagination import StandardResultsSetPagination


class StaffViewSet(viewsets.ModelViewSet):
    queryset = Staff.objects.all()
    serializer_class = StaffModelSerializer
    pagination_class = StandardResultsSetPagination
    authentication_classes = [APIAuthentication, ]

    def get_queryset(self):
        query_param = self.request.GET
        name = query_param.get('name')
        if name:
            queryset = Staff.objects.filter(name=name)
            return queryset
        return self.queryset

    def create(self, request):
        if not self.request.user.has_perm('staff.can_add_Staff'):
            return Response(data={"message": "Permission Denied"},
                            status=status.HTTP_403_FORBIDDEN)
        data = self.request.data
        serializer = StaffSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)

        serializer.save()
        return Response(data={"message": "Staff Created Successfully"},
                        status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        try:
            staff = Staff.objects.get(id=pk)
        except:
            return Response(data={"message": " This Staff is not exsits"}, status=status.HTTP_400_BAD_REQUEST)

        return Response(data=StaffModelSerializer(staff).data,
                        status=status.HTTP_200_OK)

    def update(self, request, pk=None):
        if not self.request.user.has_perm('staff.can_update_staff'):
            return Response(data={"message": "Permission Denied"},
                            status=status.HTTP_403_FORBIDDEN)
        try:
            staff = Staff.objects.get(id=pk)
        except:
            return Response(data={"message": " This Staff is not exsits"}, status=status.HTTP_400_BAD_REQUEST)

        data = self.request.data
        serializer = StaffSerializer(staff, data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        serializer.save()
        return Response(data={"message": "Staff Updated Successfully"},
                        status=status.HTTP_200_OK)
