from django.db import models
from .medicine_type import MedicineType
from .medical_history import MedicalHistory
from uuid import uuid4

class Medicine(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    medicine_type = models.ForeignKey(MedicineType, on_delete=models.CASCADE, null=False)
    name = models.CharField(max_length=255)
    date_application = models.DateTimeField()
    date_reinforcement = models.DateTimeField()
    details = models.TextField(null=True, blank=True)
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, null=False, related_name='medicines') 