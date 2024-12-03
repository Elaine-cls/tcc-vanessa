from django.db import models

class Gender(models.Model):
    id = models.IntegerField(primary_key=True, editable=False)
    description = models.CharField(max_length=255)