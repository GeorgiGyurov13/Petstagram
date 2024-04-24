from django.test import TestCase
from .models import Feedback


class FeedbackModelTestCase(TestCase):
    def setUp(self):
        self.feedback = Feedback.objects.create(helpful='Yes', comment='This is a helpful feedback.')

    def test_feedback_creation(self):
        self.assertEqual(self.feedback.helpful, 'Yes')
        self.assertEqual(self.feedback.comment, 'This is a helpful feedback.')

    def test_feedback_string_representation(self):
        expected_string = f"Feedback {self.feedback.id}"
        self.assertEqual(str(self.feedback), expected_string)

    def test_created_at_auto_now_add(self):
        self.assertIsNotNone(self.feedback.created_at)
