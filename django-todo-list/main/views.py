from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView

from .models import TodoItem


class TodoItemList(ListView):
    queryset = TodoItem.get_all()
    context_object_name = 'todo_items'
