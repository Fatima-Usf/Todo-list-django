from django.shortcuts import render
from django.http import HttpResponse
from .models import ItemTodo

# Create your views here.

def todoPlaningView(request):
    my_items = ItemTodo.objects.all()
    return render(request, 'todo.html', {'my_todo_items':my_items})