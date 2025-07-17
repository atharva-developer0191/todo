from django.contrib import admin
from .models import Task

# Register your models here.
class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'updated_at')

admin.site.register(Task, TaskAdmin)
# This will allow you to manage tasks through the Django admin interface.