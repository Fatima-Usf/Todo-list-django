from django.db import models
# Create your models here.

class ItemTodo(models.Model):
    content = models.TextField()
