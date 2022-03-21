from django.db import models
from simple_history.models import HistoricalRecords

# Create your models here.
class BaseModel(models.Model):
    """
        The Base Model For gate APP
    """
    created_at = models.DateTimeField(auto_now=True, auto_now_add=False, help_text="When This Object Created")
    updated_at = models.DateTimeField(auto_now=False, auto_now_add=True, help_text="When This Object Updated")
    history = HistoricalRecords()
    
    class Meta:
        abstract = True
        