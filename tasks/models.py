from django.db import models
# User = el modulo nos permite crear un foreingkey y relacionar 2 tablas
from django.contrib.auth.models import User

# Create your models here.

# el archivo models crea tablas sql con codigo python
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    date_completed = models.DateTimeField(null = True)
    important = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    # con funciones personaliza el panel de administracion
    def __str__(self):
        return self.title + ' by ' + self.user.username