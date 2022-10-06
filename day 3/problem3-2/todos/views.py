from contextlib import redirect_stderr
from django.shortcuts import render, redirect, get_object_or_404
from .models import Todo
from .forms import TodoForm

# Create your views here.
def index(request):
    todos = Todo.objects.all()
    context = {
        'todos':todos
    }
    return render(request, 'todos/index.html', context)

def create(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.author = request.user
            todo.save()
            return redirect('todos:index')
    else:
        form = TodoForm()
    context = {
        'form': form,
    }
    return render(request, 'todos/create.html', context)

def toggle(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.method == 'POST':
        if request.user == todo.author:
            todo.completed = True
            todo.save()
    return redirect('todos:index')

def delete(request, pk):
    todo = get_object_or_404(Todo, pk=pk)
    if request.user.is_authenticated:
        if request.user == todo.author:
            todo.delete()
            return redirect('todos:index')
    return redirect('todos:index')
