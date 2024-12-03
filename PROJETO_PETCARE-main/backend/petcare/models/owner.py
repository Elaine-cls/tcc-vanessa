from django.db import models
from .address import Address
from authentication.models import Account
from uuid import uuid4
import os

def upload_image(instance, filename):
    return f'images/{instance.id}-{filename}'

class Owner(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to=upload_image, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=13, null=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True)
    account = models.OneToOneField(Account,on_delete=models.CASCADE, null=True)
    
    def save(self, *args, **kwargs):
        if self.id:
            old_image = Owner.objects.filter(id=self.id).first()
            if old_image and old_image.photo != self.photo:
                old_image.photo.delete(save=False)

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        if self.photo:
            self.photo.delete(save=False)
        if self.address:
            self.address.delete()
        super().delete(*args, **kwargs)