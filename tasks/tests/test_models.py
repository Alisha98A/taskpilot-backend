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

    def test_is_overdue_method(self):
        """Test the is_overdue() utility method directly."""
        due_date = timezone.now() - timezone.timedelta(days=1)

        task = Task.objects.create(
            title="Overdue Check",
            description="Testing is_overdue method",
            due_date=due_date,
            owner=self.user
        )

        self.assertTrue(task.is_overdue())

    def test_set_overdue_state_method(self):
        """Test the set_overdue_state() method updates state properly."""
        due_date = timezone.now() - timezone.timedelta(days=1)

        task = Task(
            title="Manual Overdue Test",
            description="Testing set_overdue_state",
            due_date=due_date,
            owner=self.user
        )
        # Initial state should be OPEN before saving
        self.assertEqual(task.state, Task.State.OPEN)

        task.set_overdue_state()
        self.assertEqual(task.state, Task.State.OVERDUE)

    # ---------- Tests for String Representation ----------

    def test_task_str_representation(self):
        """Test the string output of a Task instance (__str__)."""
        due_date = timezone.now() + timezone.timedelta(days=3)

        task = Task.objects.create(
            title="My String Test",
            description="Testing __str__",
            due_date=due_date,
            owner=self.user
        )

        expected = f"[{task.get_priority_display()}] {task.title} — Due: {due_date:%Y-%m-%d} — Status: {task.get_state_display()}"
        self.assertEqual(str(task), expected)

    # ---------- Tests for QuerySet Ordering ----------

    def test_tasks_are_ordered_by_due_date(self):
        """Test that tasks are returned ordered by due date (ascending)."""
        task1 = Task.objects.create(
            title="First Task",
            description="Early",
            due_date=timezone.now() + timezone.timedelta(days=2),
            owner=self.user
        )
        task2 = Task.objects.create(
            title="Second Task",
            description="Later",
            due_date=timezone.now() + timezone.timedelta(days=5),
            owner=self.user
        )
        task3 = Task.objects.create(
            title="Third Task",
            description="Earliest",
            due_date=timezone.now() + timezone.timedelta(days=1),
            owner=self.user
        )

        tasks = list(Task.objects.all())
        expected_order = [task3, task1, task2]

        self.assertEqual(tasks, expected_order)