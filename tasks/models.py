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

    # ---------- Choice Fields ----------
    priority = models.CharField(
        max_length=10,
        choices=Priority.choices,
        default=Priority.MEDIUM
    )
    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.MISC
    )
    state = models.CharField(
        max_length=15,
        choices=State.choices,
        default=State.OPEN
    )

    # ---------- Timestamps ----------
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    # ---------- Utility Methods ----------
    def is_overdue(self):
        """
        Determines if the task is overdue based on the due date.
        Returns True if the task is overdue and not yet marked as 'done'.
        """
        return self.due_date < timezone.now() and self.state != self.State.DONE

    def set_overdue_state(self):
        """
        Sets the task's state to 'overdue' if it is past its due date.
        """
        if self.is_overdue():
            self.state = self.State.OVERDUE