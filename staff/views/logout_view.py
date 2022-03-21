from django.contrib.auth.models import User

from rest_framework.views import APIView
from rest_framework import status

from rest_framework.response import Response

from gate_mangment_system.authonticaton.api_authontication import APIAuthentication
from staff.models.api_key import APIKey

class LogoutView(APIView):
    """
    A simple ViewSet for listing or retrieving users.
    """
    authentication_classes = [APIAuthentication, ]

    def get(self, request):
        user = self.request.user
        token = self.request.auth
        
        if not user:
            return Response(data={"message": "User not Founded"}, status=status.HTTP_400_BAD_REQUEST)
        
        api_key = APIKey.objects.filter(key=token, user=user).last()
        if not api_key:
            return Response(data={"message": "User not Founded"}, status=status.HTTP_400_BAD_REQUEST)
        
        api_key.is_active = False
        api_key.save()
        return Response(data={"message": "Logout Successfuly"}, status=status.HTTP_200_OK)
        
