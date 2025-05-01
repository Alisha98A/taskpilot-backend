import mimetypes
from django.core.exceptions import ValidationError


def validate_file_size(value):
    """
    Validates that the uploaded file does
    not exceed the maximum allowed size (10 MB).
    """
    # Check if the value is a CloudinaryResource object
    if hasattr(value, 'size'):
        # If it is, check its size
        max_size = 10 * 1024 * 1024
        if value.size > max_size:
            raise ValidationError('File size should not exceed 10 MB')
    else:
        raise ValidationError('Uploaded file does not have a size attribute')


def validate_file_type(value):
    """
    Validates that the uploaded file is an allowed image or video type.
    """
    allowed_types = [
        'image/jpeg',
        'image/png',
        'image/gif',
        'video/mp4',
        'video/quicktime',
    ]

    # Get the file name and guess its type
    # If the file is a CloudinaryResource object
    if hasattr(value, 'name'):
        file_type, _ = mimetypes.guess_type(value.name)
    else:
        raise ValidationError('Uploaded file has no valid name attribute')

    if file_type not in allowed_types:
        raise ValidationError(
                'File type not supported. Only JPEG, PNG, GIF images and '
                'MP4/MOV videos are allowed.'
        )
