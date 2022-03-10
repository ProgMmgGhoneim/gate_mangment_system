from django.db import models

from django.utils.translation import gettext_lazy as _

from gate.base_model import BaseModel
from staff.models.visitor import Visitor

class Car(BaseModel):
    CAR_STATUS = [
        (1, _("Pending")),
        (2, _("Approved")),
        (3, _("Rejected")),
    ]
    visitor = models.ForeignKey(Visitor, null=False, blank=False, on_delete=models.CASCADE)
    plate_number  =  models.CharField(_("Plate number"), max_length=100, null=False, blank=False, db_index=True)
    color = models.CharField(_("Color"), max_length=100, blank=True, null=True, db_index=True)
    model = models.CharField(_("Model"), max_length=25, blank=True, null=True)
    status = models.IntegerField(choices=CAR_STATUS, null=False, blank=False, default=1)
    car_img = models.ImageField(null=False, blank=False, upload_to ='Cars/% Y/% m/% d/')
    
    class Meta:
        verbose_name = "Car"
        verbose_name_plural = "Cars"
        ordering = ['-created_at']
        
    def __str__(self):
        return self.plate_number