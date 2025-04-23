from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Task
from .serializers import TaskSerializer
from taskpilot_api.permissions import IsOwnerOnly

# Adapted from Django REST Framework walkthrough project
# provided by Code Institute.
# Original example used a Profile model, adapted here for Task management


# ---------- Task List View ----------
class TaskListView(APIView):
    """
    API view to retrieve all tasks for the authenticated user.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------- Task Detail View ----------
class TaskDetail(APIView):
    """
    API view to retrieve, update, or delete a single task.
    """
    serializer_class = TaskSerializer
    permission_classes = [IsOwnerOnly]

    # ---------- Helper Method ----------
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            self.check_object_permissions(self.request, task)
            return task
        except Task.DoesNotExist:
            raise Http404

    # ---------- Retrieve Task ----------
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, context={'request': request})
        return Response(serializer.data)

    # ---------- Update Task ----------
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(
            task, data=request.data, context={'request': request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
