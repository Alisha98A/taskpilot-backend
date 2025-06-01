from django.test import TestCase
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework import status
from tasks.models import Task, Note, Contact
from django.urls import reverse
from django.utils import timezone
import datetime

class TaskAPITests(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        # Create a test task
        self.task = Task.objects.create(
            owner=self.user,
            title='Test Task',
            description='Test Description',
            priority='high',
            state='todo',
            category='work',
            due_date=timezone.now() + datetime.timedelta(days=1)
        )

    def test_create_task(self):
        """Test creating a new task"""
        url = reverse('task-list')
        data = {
            'title': 'New Task',
            'description': 'New Description',
            'priority': 'medium',
            'state': 'open',
            'category': 'personal',
            'due_date': (timezone.now() + datetime.timedelta(days=1)).isoformat()
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 2)
        self.assertEqual(Task.objects.get(title='New Task').owner, self.user)

    def test_get_task_list(self):
        """Test retrieving list of tasks"""
        url = reverse('task-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_task_detail(self):
        """Test retrieving a specific task"""
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_update_task(self):
        """Test updating a task"""
        url = reverse('task-detail', args=[self.task.id])
        data = {
            'title': 'Updated Task',
            'description': self.task.description,
            'priority': 'high',
            'state': 'in_progress',
            'category': 'work',
            'due_date': self.task.due_date.isoformat()
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.task.refresh_from_db()
        self.assertEqual(self.task.title, 'Updated Task')

    def test_delete_task(self):
        """Test deleting a task"""
        url = reverse('task-detail', args=[self.task.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

class NoteAPITests(TestCase):
    def setUp(self):
        """Set up test data"""
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpass123'
        )
        self.client.force_authenticate(user=self.user)
        
        # Create a test task
        self.task = Task.objects.create(
            owner=self.user,
            title='Test Task',
            description='Test Description',
            priority='high',
            state='todo',
            category='work',
            due_date=timezone.now() + datetime.timedelta(days=1)
        )
        
        # Create a test note
        self.note = Note.objects.create(
            user=self.user,
            body='Test Note',
            task=self.task
        )

    def test_create_note(self):
        """Test creating a new note"""
        url = reverse('note-list-create')
        data = {
            'body': 'New Note',
            'task': self.task.id
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Note.objects.count(), 2)

    def test_get_note_list(self):
        """Test retrieving list of notes"""
        url = reverse('note-list-create')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_get_note_detail(self):
        """Test retrieving a specific note"""
        url = reverse('note-detail', args=[self.note.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['body'], 'Test Note')