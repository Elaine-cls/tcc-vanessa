from django.db import models
from .owner import Owner
from .gender import Gender
from .medical_history import MedicalHistory
from uuid import uuid4

class Pet(models.Model):    
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    race = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.DecimalField(null=False, decimal_places=2, max_digits=4, default=0.00)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, null=False)
    medical_history = models.OneToOneField(MedicalHistory, on_delete=models.CASCADE)
    
    