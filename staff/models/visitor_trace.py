from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

from gate.models.gate import Gate
from staff.models.car import Car
from gate.base_model import BaseModel

# Create your models here.
class VisitorTrace(BaseModel):
    VISITOR_STATUS = [
        (1, _("IN")),
        (2, _("OUT")),
    ]
    user = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE)
    gate = models.ForeignKey(Gate, null=False, blank=False, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, null=False, blank=False, on_delete=models.CASCADE)
    status = models.IntegerField(choices=VISITOR_STATUS, null=False, blank=False, default=1)

    class Meta:
        verbose_name = "Visitor History"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.user.username
        