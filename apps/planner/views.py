from django.shortcuts import render
from .models import Tasks
from .forms import TaskForm
from django.http import JsonResponse
import json
from .serializers import TaskSerializer

def daily(request):
    form = TaskForm()
    tasks = Tasks.objects.all().order_by('-date')
    return render(request, 'daily.html', {'form':form, 'tasks': tasks})

def add_task(request):
    try:
        user = request.user
        data = json.loads(request.body)
        task = data.get("task")
        date = data.get("date")
        important = data.get("important")
        completed = data.get("completed")
        print(f"Received task: {task}, Date: {date}, Important: {important}, Completed: {completed}")
        Tasks.objects.create(user=user, task=task, date=date, completed=completed, important=important)

        return JsonResponse({"status": "success", "message": "Task received", "task": task})


    except Exception as e:
        print("Error in adding task", e)
        return JsonResponse({"status": "error", "message": str(e)}, status=400)

    

def edit_task(request, taskid):
    return render(request, 'daily.html')

def delete_task(request, taskid):
    return render(request, 'daily.html')

def toggle_complete(request, taskid):
    return render(request, 'daily.html')

def toggle_important(request, taskid):
    return render(request, 'daily.html')