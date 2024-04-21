from django import forms
from .models import PetEvent


class PetEventForm(forms.ModelForm):
    class Meta:
        model = PetEvent
        fields = ['name', 'description', 'location', 'date_time']
        widgets = {
            'date_time': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M')
        }
