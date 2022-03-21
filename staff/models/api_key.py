from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from gate.base_model import BaseModel

# Create your models here.
class APIKey(BaseModel):
    
    key = models.CharField(_("Key"), max_length=256, blank=False, null=False)
    type = models.CharField(_("type"), max_length=50, blank=False, null=False)
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    is_active = models.BooleanField(_("Is Active"), default=True)
    
    class Meta:
        verbose_name = "APIKey"
        ordering = ['-created_at']

    def __str__(self):
        return self.key
        