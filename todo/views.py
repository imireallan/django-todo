from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST
from .models import Todo
from .forms import TodoForm, TodoModelForm


def index(request):
    todos = Todo.objects.all()
    # form = TodoForm()
    form = TodoModelForm()

    context = {'todos': todos, 'form': form}
    return render(request, 'todo/index.html', context)


@require_POST
def addTodo(request):
    # form = TodoForm(request.POST)

    # binding the form to Todo instance
    # todo_15 = Todo.objects.get(pk=15)
    form = TodoModelForm(request.POST)

    if form.is_valid():
        # new_todo = Todo(text=form.cleaned_data['text'])
        # new_todo.save()
        form.save()
    return redirect('index')


def complete(request, todo_id):
    todo = Todo.objects.get(pk=todo_id)
    todo.complete = True
    todo.save()
    return redirect('index')


def deleteCompleted(request):
    Todo.objects.filter(complete__exact=True).delete()
    return redirect('index')


def deleteAll(request):
    Todo.objects.all().delete()
    return redirect('index')
