from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, Note, Contact
from .serializers import (
    TaskSerializer,
    TaskWithNotesSerializer,
    NoteSerializer,
    ContactSerializer,
)
from taskpilot_api.permissions import IsOwnerOnly
import logging


# Adapted from Django REST Framework walkthrough project
# provided by Code Institute.
# Original example used a Profile model, adapted here for Task management

logger = logging.getLogger(__name__)


# ---------- Task List and Create View ----------
class TaskListView(generics.ListCreateAPIView):
    """
    API view to retrieve or create tasks for the authenticated user.
    Only returns tasks owned by the authenticated user.
    """
    serializer_class = TaskSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['priority', 'state', 'category', 'due_date']

    def get_queryset(self):
        return Task.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request):
        serializer = TaskSerializer(
            data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ---------- Task Detail, Update, and Delete View ----------
class TaskDetail(APIView):
    """
    API view to retrieve, update, or delete a specific task.
    Only the owner can perform these actions.
    """
    permission_classes = [permissions.IsAuthenticated, IsOwnerOnly]

    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404("Task not found")

    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskWithNotesSerializer(
            task, context={'request': request})
        return Response(serializer.data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        task = self.get_object(pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ---------- Note List and Create View ----------
class NoteListCreateView(generics.ListCreateAPIView):
    """
    API view to list and create notes for the authenticated user.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ---------- Note Detail View ----------
class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a specific note.
    Only allows the owner of the note to perform these actions.
    """
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        pk = self.kwargs.get("pk")
        try:
            return Note.objects.get(pk=pk, user=self.request.user)
        except Note.DoesNotExist:
            logger.warning(
                f"Note with ID {pk} not found or not owned by "
                f"{self.request.user}"
            )
            raise Http404("Note not found")


# ---------- Contact Create View ----------
class ContactCreateView(generics.CreateAPIView):
    """
    API view to create contact messages.
    Users must be authenticated to send messages.
    """
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


# ---------- Contact List View (Admin Only) ----------
class ContactListView(generics.ListAPIView):
    """
    API view to list contact messages. Only accessible by admin users.
    """
    serializer_class = ContactSerializer
    permission_classes = [permissions.IsAdminUser]

    def get_queryset(self):
        return Contact.objects.all().order_by(
            '-submitted_at'
        )
