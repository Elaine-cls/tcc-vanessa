from django.db import models
from .illness_status import IllnessStatus
from .medical_history import MedicalHistory
from uuid import uuid4

class Illness(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    illness_status = models.ForeignKey(IllnessStatus, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255)
    symptoms = models.TextField(null=True)
    description = models.TextField(null=True)
    date_diagnosis = models.DateTimeField()
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, null=False, related_name='illnesses') 