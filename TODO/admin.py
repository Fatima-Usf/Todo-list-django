from django.contrib import admin
from .models import ItemTodo
# Register your models here.

class todoitems_admin(admin.ModelAdmin):
    pass

admin.site.register(ItemTodo, todoitems_admin)