from django.contrib.auth.mixins import AccessMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import views as auth_views, login, logout, authenticate
from django.urls import reverse_lazy, reverse
from django.utils.crypto import get_random_string
from django.views import generic as views, View
from django.views.generic import TemplateView, FormView, RedirectView

from petstagram.accounts.forms import PetstagramUserCreationForm, PetstagramChangeForm, ContactForm, UserCreationForm, \
    LoginForm, ProfileUpdateForm, ForgotPasswordForm, ResetPasswordForm
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


class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/signin_user.html'

    def get(self, request):
        form = self.form_class()
        error_message = None
        return render(request, self.template_name, {'form': form, 'error_message': error_message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('home page')
            else:
                error_message = "Invalid email or password. Please try again."
                return render(request, self.template_name, {'form': form, 'error_message': error_message})


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


from django.shortcuts import render


def error_404_view(request, exception):
    # Render a template with an error message
    return render(request, 'accounts/404.html', {'message': 'Page not found'})


def error_500_view(request):
    message = "Internal Server Error. Please try again later."
    return render(request, 'accounts/500.html', {'message': message})


def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('profile_update_success')  # Redirect to a success page
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'accounts/profile_update.html', {'form': form})


def profile_update_success(request):
    return render(request, 'accounts/profile_update_success.html')


def forgot_password(request):
    if request.method == 'POST':
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = PetstagramUser.objects.get(email=email)
            except PetstagramUser.DoesNotExist:
                return HttpResponse('User with this email does not exist.')

            token = get_random_string(length=32)

            user.password_reset_token = token
            user.save()

            reset_link = f'http://127.0.0.1:8000/reset-password/{token}/'
            send_mail(
                'Reset your password',
                f'Click the following link to reset your password: {reset_link}',
                'from@example.com',
                [email],
                fail_silently=False,
            )
            return render(request, 'accounts/check_email.html')
    else:
        form = ForgotPasswordForm()
    return render(request, 'accounts/forgot_password.html', {'form': form})


def reset_password(request, token):
    try:
        user = PetstagramUser.objects.get(password_reset_token=token)
    except PetstagramUser.DoesNotExist:
        return HttpResponse('Invalid token.')

    if request.method == 'POST':
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            if new_password == confirm_new_password:
                user.set_password(new_password)
                user.save()
                user.password_reset_token = ''
                user.save()

                user = authenticate(username=user.email, password=new_password)
                login(request, user)

                return render(request, 'accounts/password_chaged.html')
            else:
                return render(request, 'accounts/reset_password.html',
                              {'form': form, 'error_message': 'Passwords do not match.'})
    else:
        form = ResetPasswordForm()

    return render(request, 'accounts/reset_password.html', {'form': form})
