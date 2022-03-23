from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.authentication import SessionAuthentication, BasicAuthentication

from django.contrib.auth.models import User

from staff.serializer.login_serilaizer import LoginSerializer
from staff.serializer.staff_serializer import StaffModelSerializer
from staff.models.staff import Staff
from gate.serializer.gate_serializer import GateSerializer

class LoginView(APIView):
    authentication_classes = [SessionAuthentication, ]

    def post(self, request, format=None):
        """
            Login View
        """
        data = request.data
        
        seriliazer = LoginSerializer(data=data)
        if not seriliazer.is_valid():
            return Response(data={"message": seriliazer.errors}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            user = User.objects.get(username=seriliazer.validated_data['username'])
        except:
            return Response(data={"message": "Invalid Username Or Password"}, status=status.HTTP_400_BAD_REQUEST)
            
        if not user.check_password(seriliazer.validated_data['password']):
            return Response(data={"message": "Invalid Password"}, status=status.HTTP_400_BAD_REQUEST)

        staff = Staff.objects.filter(user=user, is_active=True).last()
        if not staff:
            return Response(data={"message": "Username isnot Active "}, status=status.HTTP_400_BAD_REQUEST)
        
        response_data = {
            "gates":GateSerializer(staff.gate.all(), many=True).data,
            "token": staff.generate_auth_token(),
            "staff_details": StaffModelSerializer(staff).data
        }
        return Response(data=response_data, status=status.HTTP_200_OK)
