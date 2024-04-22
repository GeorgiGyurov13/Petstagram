from django.db import models
from django.contrib.auth.models import User


class PetEvent(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    likes = models.IntegerField(default=0)


