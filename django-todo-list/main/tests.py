from django.test import TestCase

from .models import TodoItem


# Create your tests here.
class TodoListTest(TestCase):
    def setUp(self):
        TodoItem.objects.create(content='hello,world')
        TodoItem.objects.create(content='good day')

    def test_create_todo_item(self):
        todo_item1 = TodoItem.objects.get(pk=1)
        todo_item2 = TodoItem.objects.get(pk=2)
        self.assertEqual(todo_item1.content, 'hello,world')
        self.assertEqual(todo_item2.content, 'good day')
