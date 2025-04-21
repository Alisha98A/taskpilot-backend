from django.db import models
from django.contrib.auth import get_user_model
from cloudinary.models import CloudinaryField
from .validators import validate_file_size, validate_file_type

# ---------- User Model ----------
User = get_user_model()

# ---------- Task Model ----------
class Task(models.Model):
    """
    Model representing a task. A task is personal and owned by a user.
    Tasks have a title, description, due date, attachment, priority, category,
    state, and tracking for creation and updates.
    """

    # ---------- Priority, State & Category Choices ----------
    class Priority(models.TextChoices):
        """Priority levels for a task."""
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    class State(models.TextChoices):
        """Possible states of a task."""
        OPEN = 'open', 'Open'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'
        OVERDUE = 'overdue', 'Overdue'

    class Category(models.TextChoices):
        """Categories to classify tasks."""
        WORK = 'work', 'Work'
        PERSONAL = 'personal', 'Personal'
        FITNESS = 'fitness', 'Fitness'
        FINANCE = 'finance', 'Finance'
        MISC = 'misc', 'Miscellaneous'

    # ---------- Core Fields ----------
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()
    attachment = CloudinaryField(
        'file',
        blank=True,
        validators=[validate_file_size, validate_file_type]
    )

    # ---------- Relationships ----------
    owner = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='tasks'
    )
    
    # ---------- Timestamps ----------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
