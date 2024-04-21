from django.db import models

# Create your models here.
# models.py
from django.db import models


class AdoptablePet(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=10)
    description = models.TextField(blank=True, null=True)
    photo = models.URLField(blank=True, null=True)
    adoption_status = models.BooleanField(default=False)
    contact_email = models.EmailField()

    def __str__(self):
        return self.name
