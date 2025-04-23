from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer

# Adapted from Django REST Framework walkthrough project
# provided by Code Institute.
# Original example used a Profile model, adapted here for Task management


# ---------- Task List View ----------
class TaskListView(APIView):
    """
    API view to retrieve all tasks.
    """

    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# ---------- Task Detail View ----------
class TaskDetail(APIView):
    serializer_class = TaskSerializer

    # ---------- Helper Method ----------
    def get_object(self, pk):
        try:
            task = Task.objects.get(pk=pk)
            return task
        except Task.DoesNotExist:
            raise Http404

    # ---------- Retrieve Task ----------
    def get(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task)
        return Response(serializer.data)

    # ---------- Update Task ----------
    def put(self, request, pk):
        task = self.get_object(pk)
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
