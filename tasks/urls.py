from django.urls import path
from tasks import views
from .views import TaskListView, TaskDetail

urlpatterns = [
    path("tasks/", TaskListView.as_view(), name="task-list"),
    path("tasks/<int:pk>/", TaskDetail.as_view(), name="task-detail"),
]