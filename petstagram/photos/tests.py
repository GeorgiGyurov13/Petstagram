from django.core.files.uploadedfile import SimpleUploadedFile
from django.core.exceptions import ValidationError
from django.test import TestCase


from petstagram.photos.models import MaxFileSizeValidator, validate_image_size_less_than_5mb, PetPhoto


class CustomValidatorsTest(TestCase):
    def test_max_file_size_validator(self):
        # Test case for MaxFileSizeValidator
        validator = MaxFileSizeValidator(limit_value=5 * 1024 * 1024)
        # File size is less than limit
        self.assertFalse(validator(SimpleUploadedFile("test.jpg", b"content")))
        # File size is greater than limit
        with self.assertRaises(ValidationError):
            validator(SimpleUploadedFile("test.jpg", b"content" * 1024 * 1024))

    def test_validate_image_size_less_than_5mb(self):
        # Test case for validate_image_size_less_than_5mb function
        file_less_than_5mb = SimpleUploadedFile("test.jpg", b"content")
        file_greater_than_5mb = SimpleUploadedFile("test.jpg", b"content" * 1024 * 1024)
        # File size is less than 5MB
        self.assertIsNone(validate_image_size_less_than_5mb(file_less_than_5mb))
        # File size is greater than 5MB
        with self.assertRaises(ValidationError):
            validate_image_size_less_than_5mb(file_greater_than_5mb)

