from django import forms
from .models import AdoptablePet


class PetCreationForm(forms.ModelForm):
    class Meta:
        model = AdoptablePet
        fields = ['name', 'age', 'gender', 'description', 'photo', 'contact_email']


