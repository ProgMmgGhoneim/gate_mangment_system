from django.db import models
from django.utils.translation import gettext_lazy as _

from gate.base_model import BaseModel

def upload_to(instance, filename):
    return 'visitor/{}'.format(filename)

class Visitor(BaseModel):
    VISITOR_STATUS = [
        (1, _("Pending")),
        (2, _("Approved")),
        (3, _("Rejected")),
    ]
    name = models.CharField(_("Name"), max_length=256, blank=False, null=False)
    address = models.CharField(_("Address"), max_length=256, blank=True, null=True)
    status = models.IntegerField(choices=VISITOR_STATUS, null=False, blank=False, default=1)
    national_id = models.CharField(_("National ID"), max_length=256, blank=False, null=False)
    job_title = models.CharField(_("Job Title"), max_length=256, blank=True, null=True)
    reason_of_visit = models.CharField(_("Reason Of Visit"), max_length=256, blank=True, null=True)
    image = models.ImageField(null=True, blank=True, upload_to =upload_to)
    
    class Meta:
        verbose_name = "Visitor"
        ordering = ['-created_at']
        unique_together = ('name', 'national_id')


    def __str__(self):
        return self.name
        