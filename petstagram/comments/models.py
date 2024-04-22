from django.db import models

from petstagram.accounts.models import PetstagramUser


# Create your models here.
class Comment(models.Model):
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(PetstagramUser, on_delete=models.CASCADE)  # Add this field
