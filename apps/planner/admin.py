from django.contrib import admin
from django.contrib.auth.models import User
from .models import Tasks

class TaskAdmin(admin.ModelAdmin):
    list_display = ('taskid', 'user', 'task', 'date', 'completed', 'important')

    def taskid(self, obj):
        return obj.taskid
    
    def user(self, obj):
        return obj.user.username
    
    def task(self, obj):
        return obj.task
    
    def date(self, obj):
        return obj.date
    
    def completed(self, obj):
        return obj.completed
    
    def important(self, obj):
        return obj.important
    
admin.site.register(Tasks, TaskAdmin)

