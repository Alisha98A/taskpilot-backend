from rest_framework import serializers
from .models import Task

# Adapted from Django REST Framework walkthrough project
# provided by Code Institute.
# Original example used a Profile model, adapted here for Task management


class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    attachment = serializers.FileField(allow_null=True, required=False)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'attachment',
            'priority', 'category', 'state',
            'created_at', 'updated_at', 'owner'
        ]
