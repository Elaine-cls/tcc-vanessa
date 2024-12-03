from django.db import models
from .address import Address
from uuid import uuid4

class Clinic(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    cnpj = models.CharField(max_length=14)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    