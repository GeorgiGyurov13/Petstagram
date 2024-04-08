from django.test import TestCase, Client
from django.urls import reverse
from .models import Pet


class PetCreateViewTest(TestCase):
    def test_pet_create_view(self):
        client = Client()
        response = client.post(reverse('create pet'), {
            'name': 'Test Pet',
            'pet_photo': 'https://example.com/pet.jpg',
            'date_of_birth': '2020-01-01'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful creation
        self.assertTrue(Pet.objects.filter(name='Test Pet').exists())


class PetEditViewTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(name='Test Pet', pet_photo='https://example.com/pet.jpg')

    def test_pet_edit_view(self):
        client = Client()
        response = client.post(reverse('edit pet', kwargs={'name': 'Doncho', 'pet_slug': self.pet.slug}), {
            'name': 'Updated Pet',
            'pet_photo': 'https://example.com/updated_pet.jpg',
            'date_of_birth': '2021-01-01'
        })
        self.assertEqual(response.status_code, 302)  # Redirects after successful edit
        self.pet.refresh_from_db()
        self.assertEqual(self.pet.name, 'Updated Pet')


class PetDetailViewTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(name='Test Pet', pet_photo='https://example.com/pet.jpg')

    def test_pet_detail_view(self):
        client = Client()
        response = client.get(reverse('details pet', kwargs={'name': 'Doncho', 'pet_slug': self.pet.slug}))
        self.assertEqual(response.status_code, 200)  # Pet detail page exists
        self.assertContains(response, 'Test Pet')  # Pet name is displayed


class PetDeleteViewTest(TestCase):
    def setUp(self):
        self.pet = Pet.objects.create(name='Test Pet', pet_photo='https://example.com/pet.jpg')

    def test_pet_delete_view(self):
        client = Client()
        response = client.post(reverse('delete pet', kwargs={'name': 'Doncho', 'pet_slug': self.pet.slug}))
        self.assertEqual(response.status_code, 302)  # Redirects after successful deletion
        self.assertFalse(Pet.objects.filter(name='Test Pet').exists())
