from operator import index
from django.db import models
from django.utils.translation import gettext_lazy as _

from gate.base_model import BaseModel

class Gate(BaseModel):
    name = models.CharField(_("Name"), max_length=256, blank=False, null=False, unique=True, db_index=True)
    description = models.CharField(_("Description"), max_length=256, blank=False, null=False)
    
    class Meta:
        verbose_name = "Gate"
        verbose_name_plural = "Gates"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.name