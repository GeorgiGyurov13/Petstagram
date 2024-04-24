from django.test import TestCase
from .models import Comment
from petstagram.accounts.models import PetstagramUser


class CommentModelTestCase(TestCase):
    def setUp(self):
        self.user = PetstagramUser.objects.create_user(email='test@example.com', password='testpassword')
        self.comment = Comment.objects.create(body='This is a test comment.', user=self.user)

    def test_comment_creation(self):
        self.assertEqual(self.comment.body, 'This is a test comment.')
        self.assertIsNotNone(self.comment.created_at)
        self.assertEqual(self.comment.user, self.user)

    def test_blank_fields(self):
        comment = Comment.objects.create(body='', user=self.user)
        self.assertEqual(comment.id, self.comment.id + 1)
