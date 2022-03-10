from django.contrib.auth.models import User

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.response import Response

from staff.serializer.user_serializer import UserSerializer

class LoginViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def create(self, request):
        pass