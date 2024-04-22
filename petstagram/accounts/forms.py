from django.contrib.auth import forms as auth_forms, get_user_model

from django import forms
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.forms import ModelForm

from petstagram.accounts.models import Profile, PetstagramUser

UserModel = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)

    def save(self, commit=True):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            raise Exception('Passwords do not match!')
        print('user register here')
        user = PetstagramUser.objects.create(email=self.cleaned_data['email'],
                                             password=make_password(self.cleaned_data['password1']))
        print(user)
        return user


class UserCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ('first_name', 'last_name', 'date_of_birth', 'profile_picture')

    def save(self, user=None, commit=True):
        profile = Profile.objects.create(
            first_name=self.cleaned_data['first_name'],
            last_name=self.cleaned_data['last_name'],
            date_of_birth=self.cleaned_data['date_of_birth'],
            profile_picture=self.cleaned_data['profile_picture'],
            user=user)
        return profile


class PetstagramChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel


