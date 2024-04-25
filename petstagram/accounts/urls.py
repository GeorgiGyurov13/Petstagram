from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import path, include
from django.conf.urls import handler404, handler500

from petstagram.accounts.views import \
    SignUpView, LoginView, \
    ProfileDetailsView, \
    ProfileUpdateView, signout_user, ProfileDeleteView, HomePageView, ContactFormView, AboutView, \
    AdminRedirectView, TermsOfUseView, SendEmailView, profile_update, profile_update_success, forgot_password, \
    reset_password

urlpatterns = (
    path("signup/", SignUpView.as_view(), name="signup user"),
    path("signin/", LoginView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),
    path("", HomePageView.as_view(), name="home page"),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('admin-redirect/', AdminRedirectView.as_view(), name='admin-redirect'),
    path('terms-of-use/', TermsOfUseView.as_view(), name='terms_of_use'),
    path('email-verification/', SendEmailView.as_view(), name='send_email_verification'),

    path(
        "profile/<int:pk>/", include([
            path("", ProfileDetailsView.as_view(), name="details profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
            path("delete/", ProfileDeleteView.as_view(), name="delete profile")
        ]),
    ),
    path('profile/update/', profile_update, name='profile_update'),
    path('profile/update/success/', profile_update_success, name='profile_update_success'),
    path('forgot-password/', forgot_password, name='forgot_password'),
    path('reset-password/<str:token>/', reset_password, name='reset_password'),
)
