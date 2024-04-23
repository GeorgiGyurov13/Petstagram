from django.db import models

class Feedback(models.Model):
    helpful_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
        ('Not sure', 'Not sure'),
    ]

    helpful = models.CharField(max_length=10, choices=helpful_choices)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Feedback {self.id}"
