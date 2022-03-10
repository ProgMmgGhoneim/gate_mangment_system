from django.db import models

from django.utils.translation import gettext_lazy as _

from gate.models.gate import Gate
from gate.base_model import BaseModel

class Camera(BaseModel):
    name = models.CharField(_("Name"), max_length=100, blank=False, unique=True, null=False, db_index=True)
    gate = models.ForeignKey(Gate, null=False, blank=False, on_delete=models.CASCADE)
    url  =  models.URLField(_("URl"), max_length=100, null=False, blank=False)
    description = models.CharField(_("Description"), max_length=256, blank=True, null=True)
    
    class Meta:
        verbose_name = "Camera"
        verbose_name_plural = "Cameras"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name