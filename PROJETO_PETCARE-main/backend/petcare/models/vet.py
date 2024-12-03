from django.db import models
from uuid import uuid4
from .clinic import Clinic
from authentication.models import Account

class Vet(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13, null=True)
    account = models.OneToOneField(Account, on_delete=models.CASCADE, default=None)
    specialization = models.CharField(max_length=255)
    clinic = models.ForeignKey(Clinic, on_delete=models.CASCADE, null=True)