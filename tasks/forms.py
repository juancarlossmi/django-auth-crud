# ModelForm = clase que permite crear formularios apartir de un modelo ya creado
from django import forms
# importacion del modelo creado en models.py
from .models import Task    

# no tenemos acceso a este formulario ya que fue construido de 
class TaskForm(forms.ModelForm):
    class Meta:
        # model = nos ayuda a inidicar el modelo que utilizaremos como base para crear el formulario
        model = Task
        # fields = agrega los campos del modelo al formulario, nombra los que desees agregar solamente
        fields = ['title', 'description', 'important']
        # widgets = nos permite estilizar un formulario creado con la classe UserCreationForn
        widgets = {
            # widgets recibe como acceso al formulario podiendo agregar clases con ("attrs") que permite agregar los atributos
            'title':forms.TextInput(attrs={'class': 'form-control', 'placeholder':'write a title'}),
            'description':forms.Textarea(attrs={'class': 'form-control', 'placeholder':'write a desciption'}),
            'important':forms.CheckboxInput(attrs={'class': 'form-check-input', 'id':'important'}),
        }