from django import forms

from petstagram.core.form_mixins import ReadonlyFieldsFormMixin
from petstagram.photos.models import PetPhoto


class PetPhotoBaseForm(forms.ModelForm):
    class Meta:
        model = PetPhoto
        fields = ('photo', 'description', 'location', 'pets')
        widgets = {
            'description': forms.TextInput(attrs={'placeholder': 'Enter description'}),
            'location': forms.TextInput(attrs={'placeholder': 'Enter location'}),
            'pets': forms.SelectMultiple(attrs={'placeholder': 'Select pets'}),
        }


class PetPhotoCreateForm(PetPhotoBaseForm):
    pass


class PetPhotoEditForm(ReadonlyFieldsFormMixin, PetPhotoBaseForm):
    readonly_fields = ("photo", "pets")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._apply_readonly_on_fields()
