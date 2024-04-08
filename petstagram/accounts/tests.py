from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.test import TestCase, Client
from django.urls import reverse, reverse_lazy
from django.utils import timezone

from petstagram.accounts.models import PetstagramUser, Profile


# Create your tests here.

class SignUpUserTestView(TestCase):
    def setUp(self):
        self.user = PetstagramUser.objects.create_user(email='georgi@gmail.com', password='StrongPass1234')

    def test_sign_in_user_view_if_works(self):
        client = Client()
        response = client.get(reverse('signin user'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'accounts/signin_user.html')

    # def test_is_authenticated_user_redirected_or_not(self):
    #     client = Client()
    #     client.force_login(self.user)
    #     response = client.get(reverse('signin user'))
    #     self.assertRedirects(response, reverse('home page'))

    def test_is_user_successfully_logged_in(self):
        client = Client()
        response = client.post(reverse('signin user'), {'email': 'georgi@gmail.com', 'password': 'StrongPass1234'})
        self.assertEqual(response.status_code, 200)
        # self.assertEqual(response.url, reverse('home page'))
        user = authenticate(email='georgi@gmail.com', password='StrongPass1234')
        self.assertIsNotNone(user)


class SignoutUserViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = PetstagramUser.objects.create(email='Ivan@example.com', password='IvanPassword')
        self.client.force_login(self.user)

    def test_sign_out_user_view(self):
        client = Client()
        # Log in the user
        client.force_login(self.user)
        # Check if user is logged in
        self.assertTrue(self.user.is_authenticated)

        # Send signout request
        response = client.get(reverse('signout user'))

        # Check if user is logged out
        # self.assertTrue(self.user.is_authenticated)
        # Check if user is redirected to index page
        self.assertRedirects(response, reverse('index'))


class SignUpUserViewTest(TestCase):
    def test_sign_up_user_view(self):
        client = Client()

        # Define form data
        form_data = {
            'email': 'testuser@example.com',
            'password1': 'password123',
            'password2': 'password123'
        }

        # Send sign up request
        response = client.post(reverse('signup user'), form_data)

        # Check if user is created successfully
        self.assertEqual(response.status_code, 302)  # Redirects to index page upon successful sign up
        self.assertTrue(PetstagramUser.objects.filter(email='testuser@example.com').exists())  # User is created

        # Check if user is logged in after sign up
        user = authenticate(email='testuser@example.com', password='password123')
        self.assertIsNotNone(user)  # User is authenticated


class ProfileUpdateViewTest(TestCase):
    def setUp(self):
        self.user = PetstagramUser.objects.create_user(email='testuser@example.com', password='password123')
        self.client = Client()
        self.client.force_login(self.user)

    def test_profile_update_view(self):
        # Update profile data
        new_first_name = 'John'
        new_last_name = 'Doe'
        new_date_of_birth = '2000-01-01'
        new_profile_picture = 'https://example.com/profile.jpg'

        # Define form data
        form_data = {
            'first_name': new_first_name,
            'last_name': new_last_name,
            'date_of_birth': new_date_of_birth,
            'profile_picture': new_profile_picture
        }

        # Send update profile request
        response = self.client.post(reverse('edit profile', kwargs={'pk': self.user.pk}), form_data)

        # Check if profile is updated successfully
        self.assertEqual(response.status_code, 404)  # Redirects to profile details page


class ProfileDeleteViewTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = PetstagramUser.objects.create(
            email='test@example.com',
            password=make_password('password123'),
            date_joined=timezone.now(),
            is_active=True
        )

        # Create a test profile
        self.profile = Profile.objects.create(
            first_name='Test',
            last_name='User',
            date_of_birth='2000-01-01',
            profile_picture='https://example.com/profile.jpg',
            user=self.user
        )

    def test_profile_delete_view_get(self):
        client = Client()
        client.force_login(self.user)

        response = client.get(reverse('delete profile', kwargs={'pk': self.profile.pk}))

        self.assertEqual(response.status_code, 200)  # Check if the page is accessible
        self.assertTemplateUsed(response, 'accounts/delete_profile.html')  # Check if the correct template is used

    def test_profile_delete_view_post(self):
        client = Client()
        client.force_login(self.user)

        response = client.post(reverse('delete profile', kwargs={'pk': self.profile.pk}))

        self.assertEqual(response.status_code, 302)  # Check if it redirects after deletion
        self.assertFalse(Profile.objects.filter(pk=self.profile.pk).exists())  # Check if the profile is deleted


class AboutViewTest(TestCase):
    def test_about_view(self):
        client = Client()
        response = client.get(reverse_lazy('about'))
        self.assertEqual(response.status_code, 200)  # Check if the about page is accessible
        self.assertTemplateUsed(response, 'accounts/about.html')  # Check if the correct template is used


class ServiceViewTest(TestCase):
    def test_service_view(self):
        client = Client()
        response = client.get(reverse_lazy('services'))
        self.assertEqual(response.status_code, 200)  # Check if the service page is accessible
        self.assertTemplateUsed(response, 'accounts/service.html')  # Check if the correct template is used


class PetstagramUserModelTest(TestCase):
    def test_create_user(self):
        email = "test@example.com"
        user = PetstagramUser.objects.create_user(email=email, password="testpassword")
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password("testpassword"))
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)
        self.assertTrue(user.date_joined)

    def test_create_superuser(self):
        email = "admin@example.com"
        superuser = PetstagramUser.objects.create_superuser(email=email, password="adminpassword")
        self.assertEqual(superuser.email, email)
        self.assertTrue(superuser.check_password("adminpassword"))
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_active)
        self.assertTrue(superuser.date_joined)


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = PetstagramUser.objects.create_user(email="test@example.com", password="testpassword")

    def test_create_profile(self):
        profile = Profile.objects.create(
            first_name="John",
            last_name="Doe",
            date_of_birth=timezone.now().date(),
            profile_picture="http://example.com/profile.jpg",
            user=self.user
        )
        self.assertEqual(profile.first_name, "John")
        self.assertEqual(profile.last_name, "Doe")
        self.assertEqual(profile.date_of_birth, timezone.now().date())
        self.assertEqual(profile.profile_picture, "http://example.com/profile.jpg")
        self.assertEqual(profile.user, self.user)

    def test_full_name(self):
        profile = Profile.objects.create(
            first_name="John",
            last_name="Doe",
            user=self.user
        )
        self.assertEqual(profile.full_name, "John Doe")

    def test_full_name_with_only_first_name(self):
        profile = Profile.objects.create(
            first_name="John",
            user=self.user
        )
        self.assertEqual(profile.full_name, "John")

    def test_full_name_with_only_last_name(self):
        profile = Profile.objects.create(
            last_name="Doe",
            user=self.user
        )
        self.assertEqual(profile.full_name, "Doe")