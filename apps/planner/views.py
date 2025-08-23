from django.shortcuts import render
from .models import Tasks
from .forms import TaskForm
from django.http import JsonResponse
import json
from .serializers import TaskSerializer

def daily(request):
    form = TaskForm()
    tasks = list(Tasks.objects.all().filter(user=request.user).order_by('date').values())
    return render(request, "daily.html", {'form':form, 'tasks':tasks})

def add_task(request):
    try:
        user = request.user
        data = json.loads(request.body)
        task = data.get("task")
        date = data.get("date")
        important = data.get("important")
        completed = data.get("completed")
        print(f"Received task: {task}, Date: {date}, Important: {important}, Completed: {completed}")
        new_task = Tasks.objects.create(user=user, task=task, date=date, completed=completed, important=important)

        return JsonResponse({
            "taskid": new_task.taskid,
            "task": task,
            "date": str(date),
            "important": important,
            "completed": completed,
        })


    except Exception as e:
        print("Error in adding task: ", e)
        return JsonResponse({"status": "error", "message": str(e)}, status=400)


def get_task(request):
    if request.method == "GET":
        tasks = list(Tasks.objects.filter(user=request.user).values('taskid', 'task', 'date', 'important', 'completed').order_by('date'))
        return JsonResponse({'tasks': tasks})

def edit_task(request, taskid):
    return render(request, 'daily.html')

def delete_task(request, taskid):
    return render(request, 'daily.html')

def toggle_complete(request, taskid):
    return render(request, 'daily.html')

def toggle_important(request, taskid):
    return render(request, 'daily.html')