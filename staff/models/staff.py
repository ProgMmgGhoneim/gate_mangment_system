import jwt
import base64

from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User
from django.conf import settings

from rest_framework import exceptions

from gate.models.gate import Gate
from gate.base_model import BaseModel
from staff.models.api_key import APIKey


class Staff(BaseModel):
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    gate = models.ManyToManyField(Gate)
    email = models.EmailField(_("E-mail"), max_length=254, null=True, blank=True)
    is_active = models.BooleanField(_("Active"), default=False)
    is_admin = models.BooleanField(_("Admin"), default=False)
    is_operation = models.BooleanField(_("Operation"), default=False)
    is_supervisor = models.BooleanField(_("Supervisor"), default=False)
    
    class Meta:
        verbose_name = "saff"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.user.username
    
    def generate_auth_token(self, type="Bearer", name="staff"):
        key = settings.API_KEY
        algorthm = settings.API_ALGORTHM
        payload = {
            "name": name,
            "id": self.id,
            "is_active": self.is_active
        }
        token =jwt.encode(payload, key, algorithm=algorthm)
        APIKey.objects.create(key=token, type=type, user=self.user, is_active=True)
        return token
    
    @staticmethod
    def from_auth_token(token):
        type, token = token.split(' ')
        if not APIKey.objects.filter(key=token, type=type, is_active=True).last():
            raise exceptions.AuthenticationFailed('Invalid Token')
        key = settings.API_KEY
        algorthm = settings.API_ALGORTHM
        data = jwt.decode(token, key, algorithms=algorthm)
        return Staff.objects.filter(id=data.get('id')).last()
        