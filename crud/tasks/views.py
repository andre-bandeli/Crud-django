from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task

def home(request):
    data = {}
    data['db'] = Task.objects.all()
    return (render(request, 'home.html', data))

def ListTasks(request):
    if request.method == "GET":
        return render(
            request, "form.html",
            {"form": TaskForm}
        )
    elif request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            user = form.save()
            return render(request, 'home.html')
