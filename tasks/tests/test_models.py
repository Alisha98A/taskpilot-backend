from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from tasks.models import Task

User = get_user_model()


class TestTaskModel(TestCase):
    # ---------- Setup ----------

    def setUp(self):
        """Create a test user for task ownership."""
        self.user = User.objects.create_user(
            username='testuser', password='testpass'
        )

    # ---------- Tests for Task Creation ----------

    def test_task_creation_defaults(self):
        """Test creating a task assigns default state, priority, and category."""
        due_date = timezone.now() + timezone.timedelta(days=2)

        task = Task.objects.create(
            title="Test Task",
            description="Test description",
            due_date=due_date,
            owner=self.user
        )

        self.assertEqual(task.state, Task.State.OPEN)
        self.assertEqual(task.priority, Task.Priority.MEDIUM)
        self.assertEqual(task.category, Task.Category.MISC)
        self.assertFalse(task.is_overdue())

    # ---------- Tests for Overdue Logic ----------

    def test_task_is_marked_overdue_on_save(self):
        """Test that a past-due task is automatically marked as overdue when saved."""
        past_due_date = timezone.now() - timezone.timedelta(days=1)

        task = Task.objects.create(
            title="Past Due Task",
            description="This task is overdue",
            due_date=past_due_date,
            owner=self.user
        )

        self.assertEqual(task.state, Task.State.OVERDUE)
        self.assertTrue(task.is_overdue())