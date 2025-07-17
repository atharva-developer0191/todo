from django.http import HttpResponse
from django.shortcuts import render, redirect
from todo.models import Task
# Create your views here.

def index(request):
    tasks = Task.objects.filter(is_completed=False)
    context ={
        'tasks': tasks
    }
    return render(request, 'home.html', context)

def addTask(request):
    task=request.POST['task']
    Task.objects.create(task=task)
    return redirect('home')