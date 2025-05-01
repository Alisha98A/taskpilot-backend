from django.contrib import admin
from .models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner', 'due_date', 'state', 'priority')
    list_filter = ('state', 'priority', 'category', 'owner')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ['due_date']