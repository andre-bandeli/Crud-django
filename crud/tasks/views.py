from django.shortcuts import redirect, render
from .forms import TaskForm
from .models import Task

def home(request):
    data = {}
    data['db'] = Task.objects.all()
    return (render(request, 'home.html', data))

def form(request):
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

def create(request):
    form = TaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/lista')
    return render(request, 'form.html', {'form': form})

def edit(request, pk):
    data = {}
    data['db'] = Task.objects.get(pk=pk)
    data['form'] = TaskForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Task.objects.get(pk=pk)
    form = TaskForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('/lista')

def delete(request, pk):
    db = Task.objects.get(pk=pk)
    db.delete()
    return redirect('/lista')