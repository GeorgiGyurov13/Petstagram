from django.test import TestCase
from .models import AdoptablePet


class AdoptablePetModelTestCase(TestCase):
    def setUp(self):
        self.pet = AdoptablePet.objects.create(
            name='Test Pet',
            age=2,
            gender='Male',
            description='This is a test pet.',
            photo='https://example.com/test.jpg',
            adoption_status=False,
            contact_email='test@example.com'
        )

    def test_pet_creation(self):
        self.assertEqual(self.pet.name, 'Test Pet')
        self.assertEqual(self.pet.age, 2)
        self.assertEqual(self.pet.gender, 'Male')
        self.assertEqual(self.pet.description, 'This is a test pet.')
        self.assertEqual(self.pet.photo, 'https://example.com/test.jpg')
        self.assertFalse(self.pet.adoption_status)
        self.assertEqual(self.pet.contact_email, 'test@example.com')

    def test_pet_string_representation(self):
        self.assertEqual(str(self.pet), 'Test Pet')
