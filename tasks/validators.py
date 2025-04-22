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


def validate_file_type(value):
    """
    Validates that the uploaded file is of an allowed type (PDF, JPEG, PNG).
    """
    allowed_types = ['application/pdf', 'image/jpeg', 'image/png']
    file_type, _ = mimetypes.guess_type(value.name)
    if file_type not in allowed_types:
        raise ValidationError(
            'File type not supported. Only PDF, JPEG, and PNG are allowed.'
        )
