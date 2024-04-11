from django.core.mail import send_mail
from django.urls import path, include

from petstagram.accounts.views import \
    SignUpUserView, SignInUserView, \
    ProfileDetailsView, \
    ProfileUpdateView, signout_user, ProfileDeleteView, HomePageView, ContactView, AboutView, ServiceView, \
    AdminRedirectView, FQAView

urlpatterns = (
    path("signup/", SignUpUserView.as_view(), name="signup user"),
    path("signin/", SignInUserView.as_view(), name="signin user"),
    path("signout/", signout_user, name="signout user"),
    path("", HomePageView.as_view(), name="home page"),
    path('contact/', ContactView.as_view(), name='contact'),
    path('about/', AboutView.as_view(), name='about'),
    path('services/', ServiceView.as_view(), name='services'),
    path('admin-redirect/', AdminRedirectView.as_view(), name='admin-redirect'),
    path('FQA/', FQAView.as_view(), name='FQA'),

    path(
        "profile/<int:pk>/", include([
            path("details/", ProfileDetailsView.as_view(), name="details profile"),
            path("edit/", ProfileUpdateView.as_view(), name="edit profile"),
            path("delete/", ProfileDeleteView.as_view(), name="delete profile")
        ]),
    )
)
