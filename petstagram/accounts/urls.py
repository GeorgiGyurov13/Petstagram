from django.core.mail import send_mail
from django.urls import path, include

from petstagram.accounts.views import \
    SignUpView, SignInUserView, \
    ProfileDetailsView, \
    ProfileUpdateView, signout_user, ProfileDeleteView, HomePageView, ContactFormView, AboutView, ServiceView, \
    AdminRedirectView, FQAView, TermsOfUseView, SendEmailView

urlpatterns = (
    path("signup/", SignUpView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),
    path("", HomePageView.as_view(), name="home page"),
    path('contact/', ContactFormView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServiceView.as_view(), name='services'),
    path('admin-redirect/', AdminRedirectView.as_view(), name='admin-redirect'),
    path('FQA/', FQAView.as_view(), name='FQA'),
    path('terms-of-use/', TermsOfUseView.as_view(), name='terms_of_use'),
    path('email-verification/', SendEmailView.as_view(), name='send_email_verification'),

    path(
        "profile/<int:pk>/", include([
            path("details/", ProfileDetailsView.as_view(), name="details profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
            path("delete/", ProfileDeleteView.as_view(), name="delete profile")
        ]),
    )
)
