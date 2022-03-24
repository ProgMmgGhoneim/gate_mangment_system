from django.contrib.auth.models import User


from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, status
from rest_framework.response import Response

from gate_mangment_system.authonticaton.api_authontication import APIAuthentication
from staff.serializer.report_serializer import ReportSerializer
from staff.serializer.car_serializer import CarSerializer
from staff.serializer.visitor_serilaizer import VisitorSerializer
from gate.serializer.gate_serializer import GateSerializer
from staff.models.report import Report
from staff.models.car import Car
from staff.models.visitor import Visitor
from staff.models.visitor_trace import VisitorTrace
from gate.models.gate import Gate


class ReportViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    authentication_classes = [APIAuthentication, ]
    serializer_class = ReportSerializer
    permission_classes = [IsAuthenticated]

    @staticmethod
    def get_model_serializer(key):
        str_to_model = {
            'VISITOR': (Visitor, VisitorSerializer),
            'CAR': (Car, CarSerializer),
            'VisitorTrace': (VisitorTrace, ),
            'GATE': (Gate, GateSerializer)
        }
        return str_to_model.get(key)

    def create(self, request):
        import ipdb
        ipdb.set_trace()
        if not self.request.user.has_perm('staff.can_make_report'):
            return Response(data={"message": "Permission Denied"},
                            status=status.HTTP_403_FORBIDDEN)
        data = self.request.data
        serializer = ReportSerializer(data=data)
        if not serializer.is_valid():
            return Response(data={"message": serializer.errors},
                            status=status.HTTP_400_BAD_REQUEST)
        report_type = serializer.validated_data['report_type']
        model, ser = self.get_model_serializer(report_type)

        report = model.objects.filter(created_at__range=[serializer.validated_data['start_at'],
                                                         serializer.validated_data['end_at']])
        file_name = 'report_{}_{}.xls'.format(serializer.validated_data['start_at'],
                                              serializer.validated_data['end_at'])

        file_path = Report.get_or_create_file_path(filename=file_name)
        report = Report.create_report_object(filename=file_name,
                                             path=file_path)
        return Response(data={"message": ser(report, many=True).data})
