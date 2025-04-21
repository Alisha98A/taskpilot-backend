from django.db import models
from django.contrib.auth import get_user_model

# ---------- User Model ----------
User = get_user_model()

# ---------- Task Model ----------
class Task(models.Model):
    """
    Model representing a task. A task is personal and owned by a user.
    Tasks have a title, description, due date, attachment, priority, category,
    state, and tracking for creation and updates.
    """

    # ---------- Core Fields ----------
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    due_date = models.DateTimeField()