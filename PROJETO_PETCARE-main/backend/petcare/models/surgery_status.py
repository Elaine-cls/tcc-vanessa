from django.db import models

class SurgeryStatus(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    status = models.CharField(max_length=155)