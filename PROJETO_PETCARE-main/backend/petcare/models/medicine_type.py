from django.db import models

class MedicineType(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    type = models.CharField(max_length=155)