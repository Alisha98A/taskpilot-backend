from django.urls import path
from tasks import views

urlpatterns = [
    path('tasks/', views.TaskListView.as_view(), name='tasks'),
    path('tasks/<int:pk>/', views.TaskDetail.as_view()),
]