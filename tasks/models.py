from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

# ---------- User Model ----------
User = get_user_model()


# ---------- Task Model ----------
class Task(models.Model):
    """
    Model representing a task. A task is personal and owned by a user.
    Tasks have a title, description, due date, priority, category,
    state, and tracking for creation and updates.
    """

    # ---------- Priority, State & Category Choices ----------
    class Priority(models.TextChoices):
        """ Priority levels for a task. """
        LOW = 'low', 'Low'
        MEDIUM = 'medium', 'Medium'
        HIGH = 'high', 'High'

    class State(models.TextChoices):
        """ Possible states of a task. """
        OPEN = 'open', 'Open'
        IN_PROGRESS = 'in_progress', 'In Progress'
        DONE = 'done', 'Done'
        OVERDUE = 'overdue', 'Overdue'

    class Category(models.TextChoices):
        """ Categories to classify tasks. """
        WORK = 'work', 'Work'
        PERSONAL = 'personal', 'Personal'
        FITNESS = 'fitness', 'Fitness'
        FINANCE = 'finance', 'Finance'
        MISC = 'misc', 'Miscellaneous'

    # ---------- Core Fields ----------
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()

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

    # ---------- Model Meta Options ----------
    class Meta:
        ordering = ['due_date']
        verbose_name = "Task"
        verbose_name_plural = "Tasks"

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

    # ---------- Save Method Override ----------
    def save(self, *args, **kwargs):
        """
        Overrides the save method to check
        if the task is overdue before saving.
        """
        self.set_overdue_state()
        super().save(*args, **kwargs)

    # ---------- String Representation ----------
    def __str__(self):
        """
        String representation of the Task object.
        Shows priority, title, formatted due date, and human-readable state.
        """
        return (
            f"[{self.get_priority_display()}] {self.title} — "
            f"Due: {self.due_date:%Y-%m-%d} — "
            f"Status: {self.get_state_display()}"
        )


class Note(models.Model):
    """
    Model representing a note attached to a task.
    Notes are created by users and linked to tasks.
    """
    # ---------- Relationships ----------
    task = models.ForeignKey(
        Task, on_delete=models.CASCADE, related_name='notes'
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='notes'
    )

    # ---------- Core Fields ----------
    body = models.TextField()

    # ---------- Timestamps ----------
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    # ---------- Model Meta Options ----------
    class Meta:
        ordering = ['-date_added']

    # ---------- String Representation ----------
    def __str__(self):
        return f"Note by {self.user.username} on {self.task.title}"


class Contact(models.Model):
    """
    Feedback or issue report submitted by a user.
    """
    # ---------- Relationships ----------
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, blank=True)

    # ---------- Core Fields ----------
    subject = models.CharField(max_length=255)
    message = models.TextField()
    email = models.EmailField(max_length=255, null=True, blank=True)

    # ---------- Timestamps ----------
    submitted_at = models.DateTimeField(auto_now_add=True)

    # ---------- Save Method Override ----------
    def save(self, *args, **kwargs):
        # Use the user’s account email if none is manually provided.
        if not self.email and self.user:
            self.email = self.user.email
        super().save(*args, **kwargs)

    # ---------- String Representation ----------
    def __str__(self):
        return f"{self.subject} ({self.user.username})"
