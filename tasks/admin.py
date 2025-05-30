from django.contrib import admin
from .models import Task, Note
from .models import Contact

admin.site.register(Contact)

class NoteInline(admin.TabularInline):
    model = Note
    extra = 1
    readonly_fields = ('date_added', 'date_updated')
    fields = ('user', 'body', 'date_added', 'date_updated')
    show_change_link = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'owner', 'due_date', 'state', 'priority')
    list_filter = ('state', 'priority', 'category', 'owner')
    search_fields = ('title', 'description', 'owner__username')
    ordering = ['due_date']
    inlines = [NoteInline]