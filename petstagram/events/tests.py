from django.test import TestCase
from .models import PetEvent


class PetEventModelTestCase(TestCase):
    def setUp(self):
        self.event = PetEvent.objects.create(
            name='Test Event',
            description='This is a test event.',
            location='Test Location',
            date_time='2022-01-01 12:00:00',
            likes=0
        )

    def test_event_creation(self):
        self.assertEqual(self.event.name, 'Test Event')
        self.assertEqual(self.event.description, 'This is a test event.')
        self.assertEqual(self.event.location, 'Test Location')
        self.assertEqual(self.event.date_time, '2022-01-01 12:00:00')
        self.assertEqual(self.event.likes, 0)

    def test_likes_increment(self):
        self.event.likes += 1
        self.event.save()
        self.assertEqual(self.event.likes, 1)

    def test_likes_decrement(self):
        self.event.likes -= 1
        self.event.save()
        self.assertEqual(self.event.likes, -1)
