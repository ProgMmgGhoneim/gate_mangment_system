from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response

class ReportViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    queryset = User.objects.all()
    serializer_class = "UserSerializer"
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        pass

    def list(self, request):
        pass

    def create(self, request):
        pass

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass