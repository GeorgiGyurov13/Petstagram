from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import views as auth_views, login, logout
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.views.generic import TemplateView, FormView, RedirectView

from petstagram.accounts.forms import PetstagramUserCreationForm, PetstagramChangeForm, ContactForm, UserCreationForm
from petstagram.accounts.models import PetstagramUser, Profile
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from petstagram.common.models import PhotoLike
from petstagram.pets.models import Pet
from petstagram.photos.models import PetPhoto


class OwnerRequiredMixin(AccessMixin):
    """Verify that the current user has this profile."""

    def dispatch(self, request, *args, **kwargs):
        if request.user.pk != kwargs.get('pk', None):
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


class SignInUserView(LoginView):
    template_name = "accounts/signin_user.html"
    redirect_authenticated_user = True
    success_url = reverse_lazy('home page')


class SignUpView(TemplateView):
    form_class_user = PetstagramUserCreationForm
    form_class_profile = UserCreationForm
    template_name = 'accounts/signup_user.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_user'] = self.form_class_user()
        context['form_profile'] = self.form_class_profile()
        return context

    def post(self, request, *args, **kwargs):
        form_user = self.form_class_user(request.POST)
        form_profile = self.form_class_profile(request.POST)

        if form_user.is_valid() and form_profile.is_valid():
            return self.forms_valid(form_user, form_profile)
        else:
            return self.forms_invalid(form_user, form_profile)

    def forms_valid(self, form_user, form_profile):
        try:
            user = form_user.save()
            print(user)
            form_profile.save(user=user)

            login(self.request, user)

            return redirect('home page')
        except Exception as e:
            if str(e) == 'Passwords do not match!':
                form_user.add_error('password', 'Passwords do not match!')
            return self.forms_invalid(form_user, form_profile)

    def forms_invalid(self, form_user, form_profile):
        return render(self.request, self.template_name, {'form_user': form_user, 'form_profile': form_profile})


def signout_user(request):
    logout(request)
    return redirect('home page')


class ProfileDetailsView(views.DetailView):
    queryset = Profile.objects \
        .prefetch_related("user") \
        .all()

    template_name = "accounts/details_profile.html"

    def get_object(self, queryset=None):
        # Fetch the user ID from the URL
        user_id = self.kwargs.get('pk')
        # Query the profile associated with the user ID
        profile = get_object_or_404(Profile, user_id=user_id)
        return profile


class ProfileUpdateView(views.UpdateView):
    queryset = Profile.objects.all()
    template_name = "accounts/edit_profile.html"
    fields = ("first_name", "last_name", "date_of_birth", "profile_picture")

    def get_success_url(self):
        return reverse("details profile", kwargs={
            "pk": self.object.pk,
        })

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)

        form.fields["date_of_birth"].widget.attrs["type"] = "date"
        form.fields["date_of_birth"].label = "Birthday"
        return form


class ProfileDeleteView(views.DeleteView):
    queryset = Profile.objects.all()
    template_name = "accounts/delete_profile.html"
    success_url = reverse_lazy('index')


class HomePageView(TemplateView):
    template_name = 'accounts/home_page.html'


# contact/views.py

class ContactFormView(FormView):
    template_name = 'accounts/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('send_email_verification')

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']

        # Send email
        send_mail(
            subject='New message from your website',
            message=message,
            from_email=email,
            recipient_list=('gyurovgeorgi740@gmail.com',),
            fail_silently=False,
        )

        return super().form_valid(form)


class AboutView(TemplateView):
    template_name = 'accounts/about.html'


class AdminRedirectView(RedirectView):
    url = reverse_lazy('admin:index')


class FQAView(TemplateView):
    template_name = 'accounts/FQA.html'


class TermsOfUseView(TemplateView):
    template_name = 'accounts/terms_of_use.html'


class SendEmailView(TemplateView):
    template_name = 'accounts/welcome_email.html'


def about_page(request):
    team_members = Profile.objects.all()
    return render(request, 'accounts/about.html', {'team_members': team_members})


def testimonial_view(request):
    quotes = [
        {
            'quote': "Petstagram is more than just an app—it's a family of pet enthusiasts united by their love for all creatures great and small.",
            'author': "Ivan Petrov"
        },
        {
            'quote': "At Petstagram, we're on a mission to make the world a happier place—one pet post at a time.",
            'author': "Lecho Lechev"
        }
    ]
    return render(request, 'accounts/home_page.html', {'quotes': quotes})
