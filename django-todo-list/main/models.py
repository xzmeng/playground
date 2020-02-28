from django.db import models


# Create your models here.
class TodoItem(models.Model):
    content = models.CharField(max_length=1024, verbose_name='todo-item')
    time_created = models.DateTimeField(auto_now_add=True, verbose_name='time created')

    @classmethod
    def get_all(cls):
        return cls.objects.all().order_by('-time_created')
