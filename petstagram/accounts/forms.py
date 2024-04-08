from django.contrib.auth import forms as auth_forms, get_user_model

from django import forms
from django.core.mail import send_mail

UserModel = get_user_model()


class ContactForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

    def send_email(self):
        name = self.cleaned_data['name']
        email = self.cleaned_data['email']
        message = self.cleaned_data['message']
        send_mail(
            f"Message from {name}",
            message,
            email,
            ['your@email.com'],  # Change to your email address
            fail_silently=False,
        )


class PetstagramUserCreationForm(auth_forms.UserCreationForm):
    user = None

    class Meta(auth_forms.UserCreationForm.Meta):
        model = UserModel
        fields = ('email',)


class PetstagramChangeForm(auth_forms.UserChangeForm):
    class Meta(auth_forms.UserChangeForm.Meta):
        model = UserModel
