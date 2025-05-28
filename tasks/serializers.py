from django.contrib.humanize.templatetags.humanize import naturaltime
from rest_framework import serializers
from .models import Task, Note, Contact
from .validators import validate_file_size, validate_file_type

# Adapted from Django REST Framework walkthrough project
# provided by Code Institute.
# Original example used a Profile model, adapted here for Task management


# ---------------- Task Serializer ----------------
class TaskSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    attachment = serializers.FileField(
        allow_null=True,
        required=False,
        validators=[validate_file_size, validate_file_type]
    )
    is_owner = serializers.SerializerMethodField()
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_is_owner(self, obj):
        request = self.context.get('request')
        if request and hasattr(request, 'user'):
            return request.user == obj.owner
        return False

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)

    class Meta:
        model = Task
        fields = [
            'id', 'title', 'description', 'due_date', 'attachment',
            'priority', 'category', 'state',
            'created_at', 'updated_at', 'owner', 'is_owner'
        ]


# ---------------- Note Serializer ----------------
class NoteSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.none())

    class Meta:
        model = Note
        fields = ['id', 'task', 'user', 'body', 'date_added', 'date_updated']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get('request', None)
        if request and request.user.is_authenticated:
            self.fields['task'].queryset = Task.objects.filter(
                owner=request.user
                )


# ---------------- Task with Notes Serializer ----------------
class TaskWithNotesSerializer(TaskSerializer):
    notes = NoteSerializer(many=True, read_only=True)

    class Meta(TaskSerializer.Meta):
        fields = TaskSerializer.Meta.fields + ['notes']


# ---------------- Contact Serializer ----------------
class ContactSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Contact
        fields = ['id', 'user', 'email', 'subject', 'message', 'submitted_at']