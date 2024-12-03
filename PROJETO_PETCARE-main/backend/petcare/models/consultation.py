from django.db import models
from uuid import uuid4
from .vet import Vet
from .clinic import Clinic
from .medical_history import MedicalHistory

class Consultation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    reason = models.TextField(null=False)
    date = models.DateTimeField()
    vet = models.ForeignKey(Vet, on_delete=models.CASCADE)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE)
    medical_history = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, null=False, related_name='queries') 