from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from tasks import validators


class ValidatorTests(TestCase):
    # Test that a small file (about 5KB) passes the size validation
    def test_validate_file_size_valid(self):
        file = SimpleUploadedFile("test.pdf", b"12345" * 1024)  # ~5KB
        self.assertIsNone(validators.validate_file_size(file))