from django.contrib import admin

from apps.todo.models import Task
# Register your models here.
@admin.register(Task)
class ToDoAdmin(admin.ModelAdmin):
    list_display = ['title', 'completed', 'created']
    search_fields = ['title']
    list_per_page = 20