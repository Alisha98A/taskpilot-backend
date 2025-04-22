from django.core.exceptions import ValidationError
from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from tasks import validators


class ValidatorTests(TestCase):
    # Test that a small file (about 5KB) passes the size validation
    def test_validate_file_size_valid(self):
        file = SimpleUploadedFile("test.pdf", b"12345" * 1024)  # ~5KB
        self.assertIsNone(validators.validate_file_size(file))

    # Test that an oversized file (11MB) triggers a ValidationError
    def test_validate_file_size_invalid(self):
        file = SimpleUploadedFile(
            "bigfile.pdf",
            b"0" * (11 * 1024 * 1024))  # 11MB
        with self.assertRaises(ValidationError):
            validators.validate_file_size(file)

    # Test that a valid PDF file passes the file type validation
    def test_validate_file_type_valid_pdf(self):
        file = SimpleUploadedFile("test.pdf", b"dummy content")
        self.assertIsNone(validators.validate_file_type(file))

    # Test that a disallowed file type (.exe) triggers a ValidationError
    def test_validate_file_type_invalid(self):
        file = SimpleUploadedFile("test.exe", b"dummy content")
        with self.assertRaises(ValidationError):
            validators.validate_file_type(file)
