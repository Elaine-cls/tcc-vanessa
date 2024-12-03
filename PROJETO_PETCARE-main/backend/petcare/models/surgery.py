from django.db import models
from .surgery_status import SurgeryStatus
from .medical_history import MedicalHistory
from uuid import uuid4

class Surgery(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    surgery_status = models.ForeignKey(SurgeryStatus, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255)
    details = models.TextField(null=True)
    date = models.DateTimeField()
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, null=False, related_name='surgeries') 