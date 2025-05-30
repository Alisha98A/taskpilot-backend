from django.urls import path
from .views import (
    TaskListView, TaskDetail,
    NoteListCreateView, NoteDetailView, ContactCreateView, ContactListView
)

urlpatterns = [
    path('tasks/', TaskListView.as_view(), name='task-list'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),

    path('notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),

    path('contact/', ContactCreateView.as_view(), name='contact-create'),
    path('contact/messages/', ContactListView.as_view(), name='contact-list'),
]
