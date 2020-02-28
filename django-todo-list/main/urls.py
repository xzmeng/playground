from django.urls import path

from . import views

urlpatterns = [
    path('todo-items/', views.TodoItemList.as_view(), name='todo-item-list'),
]