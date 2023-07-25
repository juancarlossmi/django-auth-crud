from django.contrib import admin
from .models import Task

# Register your models here.

class Task_Admin(admin.ModelAdmin):
    # cuando queremos que solo un campo sea "readonly_field" debemos agrear una coma ya que solo recibe como parametro una tupla
    readonly_fields=('created',)

admin.site.register(Task, Task_Admin)