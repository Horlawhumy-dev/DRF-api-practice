from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
     
    fields = ['owner', 'title', 'completed']

    search_fields = ['title', 'owner']

    filter_fields = ['title']

    editable_fields = ['title', 'owner']

admin.site.register(Task,TaskAdmin)