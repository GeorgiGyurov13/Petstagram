from django.test import TestCase, Client
from django.urls import reverse
from .models import PhotoLike
from .views import IndexView, like_pet_photo
from ..accounts.models import PetstagramUser, Profile


class IndexViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = PetstagramUser.objects.create(email='test@example.com')
        self.profile = Profile.objects.create(user=self.user)

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/index.html')

    def test_index_view_with_pet_name_pattern(self):
        response = self.client.get(reverse('index'), {'pet_name_pattern': 'test'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'common/index.html')


class LikePetPhotoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = PetstagramUser.objects.create(email='test@example.com')
        self.photo_like = PhotoLike.objects.create(pet_photo_id=1, user=self.user)

    # def test_like_pet_photo(self):
    #     response = self.client.get(reverse('like_pet_photo', kwargs={'pk': self.photo_like.pet_photo_id}),
    #                                HTTP_REFERER=None)
    #     self.assertEqual(response.status_code, 302)  # Redirects after like
    #
    # def test_dislike_pet_photo(self):
    #     response = self.client.get(reverse('like_pet_photo', kwargs={'pk': self.photo_like.pet_photo_id}),
    #                                HTTP_REFERER=None)
    #     self.assertEqual(response.status_code, 302)  # Redirects after dislike


class ProfileModelTest(TestCase):
    def setUp(self):
        self.user = PetstagramUser.objects.create(email='test@example.com')

    def test_profile_full_name(self):
        profile = Profile.objects.create(user=self.user, first_name='John', last_name='Doe')
        self.assertEqual(profile.full_name, 'John Doe')

# class PhotoLikeModelTest(TestCase):
#     def setUp(self):
#         # Create test user
#         self.user = PetstagramUser.objects.create(email='test@example.com')
#
#     def test_photo_like_creation(self):
#         photo_like = PhotoLike.objects.create(pet_photo_id=1, user=self.user)
#         self.assertTrue(isinstance(photo_like, PhotoLike))
