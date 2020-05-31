from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import ItemTodo

# Create your views here.

def todoPlaningView(request):
    my_items = ItemTodo.objects.all()
    return render(request, 'todo.html', {'my_todo_items':my_items})


def add_item(request):
    #get the content that the user added in the form by post 
    #content = request.POST['content'] then add it to my db via ItemTodo() model class
    new_item = ItemTodo(content = request.POST['content'])
    new_item.save() #save my new item in my db
    return HttpResponseRedirect('/todo/')