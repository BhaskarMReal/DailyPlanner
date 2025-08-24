from django.shortcuts import render
from .models import Tasks
from .forms import TaskForm
from django.http import JsonResponse
import json
from .serializers import TaskSerializer
from django.contrib import sessions
from django.utils import timezone

def daily(request):
    form = TaskForm()
    tasks = list(Tasks.objects.all().filter(user=request.user).order_by('date').values())
    return render(request, "daily.html", {'form':form, 'tasks':tasks})

def all(request):
    form = TaskForm()
    tasks = list(Tasks.objects.all().filter(user=request.user).order_by('date').values())
    return render(request, "all.html", {'form':form, 'tasks':tasks})

def important(request):
    form = TaskForm()
    tasks = list(Tasks.objects.all().filter(user=request.user).order_by('date').values())
    return render(request, "important.html", {'form':form, 'tasks':tasks})

def completed(request):
    form = TaskForm()
    tasks = list(Tasks.objects.all().filter(user=request.user).order_by('date').values())
    return render(request, "completed.html", {'form':form, 'tasks':tasks})

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
    if request.method == "POST":
        data = json.loads(request.body)
        filter = data.get("current_url")
        if filter == "daily":
            date_today = timezone.localdate()
            tasks = list(Tasks.objects.filter(user=request.user, date=date_today).values('taskid', 'task', 'date', 'important', 'completed').order_by('date'))
        elif (filter == "all"):
            tasks = list(Tasks.objects.filter(user=request.user).values('taskid', 'task', 'date', 'important', 'completed').order_by('date'))
        elif (filter == "important"):
            tasks = list(Tasks.objects.filter(user=request.user, important=True).values('taskid', 'task', 'date', 'important', 'completed').order_by('date'))
        elif (filter == "completed"):
            tasks = list(Tasks.objects.filter(user=request.user, completed=True).values('taskid', 'task', 'date', 'important', 'completed').order_by('date'))
        return JsonResponse({'tasks': tasks})

def edit_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        taskId = data.get("taskid")
        edit_current_task = Tasks.objects.filter(taskid=taskId, user=request.user).first()
        return JsonResponse({
            "task": edit_current_task.task,
            "date": edit_current_task.date,
            "important": edit_current_task.important,
            "completed": edit_current_task.completed
        })
     
def save_edit_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data)
        taskId = data.get("taskid")
        task = data.get("task")
        date = data.get("date")
        important = data.get("important")
        completed = data.get("completed")
        print("Retrieved Object: ", Tasks.objects.filter(taskid=taskId))
        Tasks.objects.filter(taskid=taskId).update(task=task, date=date, important=important, completed=completed)
        return JsonResponse({'status':'success', 'message': 'task updated'})

def delete_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        taskId= data.get('taskid')
        delete_obj = Tasks.objects.all().filter(taskid=taskId, user=request.user)
        delete_obj.delete()
        return JsonResponse({'status':'success', 'message': 'task deleted'})





def toggle_complete(request):
    return render(request, 'daily.html')

def toggle_important(request, taskid):
    return render(request, 'daily.html')