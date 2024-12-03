from django.db import models
from uuid import uuid4

class Address(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    cep = models.CharField(max_length=8)