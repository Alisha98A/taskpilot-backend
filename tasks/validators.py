import mimetypes
from django.core.exceptions import ValidationError


def validate_file_size(value):
    """
    Validates that the uploaded file does
    not exceed the maximum allowed size (10 MB).
    """
    max_size = 10 * 1024 * 1024
    if value.size > max_size:
        raise ValidationError('File size should not exceed 10 MB')