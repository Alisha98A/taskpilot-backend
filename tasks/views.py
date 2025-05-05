from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions, generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, Note
from .serializers import TaskSerializer, NoteSerializer
from taskpilot_api.permissions import IsOwnerOnly

# Adapted from Django REST Framework walkthrough project
# provided by Code Institute.
# Original example used a Profile model, adapted here for Task management


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
            data=request.data, context={'request': request})
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
        # Include related notes in the task response
        notes = Note.objects.filter(task=task)
        task_data = TaskSerializer(task, context={'request': request}).data
        task_data['notes'] = NoteSerializer(notes, many=True).data
        return Response(task_data)

    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, data=request.data, context={'request': request})
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

    def get_queryset(self):
        return Note.objects.filter(user=self.request.user)