from django.contrib.auth.models import User

from rest_framework import authentication, exceptions

from staff.models.staff import Staff

class APIAuthentication(authentication.BaseAuthentication):
    
    def get_from_header(self, request):
        return request.META.get("HTTP_AUTHORIZATION")
    
    def authenticate(self, request):
        get_token = self.get_from_header(request)
        if not get_token:
            raise exceptions.AuthenticationFailed('Authontication Failed')
        try:
            staff = Staff.from_auth_token(get_token)
        except User.DoesNotExist:
            raise exceptions.AuthenticationFailed('No such user')
        return (staff.user, get_token)
    
    def authenticate_header(self, request):
        return 'Bearer'