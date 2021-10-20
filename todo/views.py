from django.shortcuts import render, redirect
from .models import Todo
from .forms import TodoAddForm


def home(request):
    return render(request, "todo/home.html")

def todo_list(request):
    todos = Todo.objects.all()
    context = {
        'todos' : todos
    }
    
    return render(request, "todo/todo_list.html", context)

def todo_add(request):
    
    form = TodoAddForm()
    
    if request.method == "POST":
        form = TodoAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
    
    context = {
        'form' : form,
    }
    
    return render(request, "todo/todo_add.html", context)

def todo_update(request,id):
    todo = Todo.objects.get(id=id)
    form = TodoAddForm(instance=todo)
    
    if request.method == 'POST':
        form = TodoAddForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            return redirect('list')
    context = {
        "todo": todo,
        "form": form,
    }
    
    return render(request, "todo/todo_update.html", context)
    