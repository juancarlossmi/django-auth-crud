from django.shortcuts import render, redirect, get_object_or_404
# UserCreationForm = sirve para crear usuario, AuthenticationForm = sirve para comprobar si ya existe un usuario
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# User = modulo que permite crear un usuario con login y logout por default
from django.contrib.auth.models import User
# login = permite hacer login con un User, logout = elimina la informacion del inicio de sesion de un usuario ("elimina el cookie del usuario"), authenticated = comprueba la informacion ingresada en el form para saber que informacion se recibe y comprobar si se encuentra en la base de datos
from django.contrib.auth import login, logout, authenticate
# IntegrityError: ocurre cuando guardamos un dato que ya existe y lo hemos clasificado como unico
from django.db import IntegrityError
# importamos el formulario personalizado
from .forms import TaskForm, Task
# timezone = modulo que muestra la fecha y hora actual
from django.utils import timezone
# login_required = decorador especial que protegue una url haciendo que solo los usuario logeados tengan acceso a cieras partes de la pagina en donde un usuaio debe estar logeado para ver esa parte de la pagina
from django.contrib.auth.decorators import login_required
# datetime = lo utilizamos para saludar al usuario logeada indicando una condicion si es dia tarde o noche muestra mensajes diferentes
from datetime import datetime

# Create your views here.

# home = funcion que muestra la pagina de inicio de una app
def home(request):
    now = datetime.now()
    hour = now.hour
    if 6 <= hour < 12:
        greeting = 'Good morning: ' + request.user.username
        css_class = 'morning'
    elif 12 <= hour < 19:
        greeting = 'Good afternoon: ' + request.user.username
        css_class = 'afternoon'
    else:
        greeting = 'Good night: ' + request.user.username
        css_class = 'night'
    return render(request, 'home.html', {'greeting':greeting, 'css_class':css_class})



# signup = funcion que rei¿gistra a un usuario y valida que la contrasela 1 y 2 sean iguales
def signup(request):
    if request.method == 'GET':
        # con request.POST obtenemos lo que haya ingresado el usuario en el formulario
        return render(request, 'signup.html', {
        # UserCreationForm = formulario para registrar usuarios ("username, password")
            'form':UserCreationForm
        })
    else:
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        username = request.POST.get('username', '')

        if not username or not password1 or not password2:
            # Si uno o ambos campos están vacíos, mostrar un mensaje de error.
            return render(request, 'signup.html', {
                'form': UserCreationForm,
                'error':'password and username cannot be empty'
            })

        # de esta forma utilizamos las propiedades del UserCreationForm, y validamos si las 2 contraseñas ingresada coinciden para poder crear un nuevo usuario
        if request.POST['password1'] == request.POST['password2']:
            # la base de datos donde guardamos el usuario tiene sus propias validadciones y para poder controlar posibles errores al ingresar a la base de datos por django debemos encapsular esa consulta en un try y except para controlar errores de consulta en la base de datos
            try:
                # con User creamos un nuevo usuario con los datos ingresados en el formulario
                user = User.objects.create_user(username = request.POST['username'], password = request.POST['password1'])
                # con la instruccion "SAVE" almacenamos en db.sqlite3 el nombre de usuario y las contraseñas ingresadas en el formulario
                user.save()
                # con HttpResponse = podemos generar codigo html dentro de los parentesis
                # return HttpResponse('created user successfully')
                # login = es una metodo que nos permite crear una cookie del usuario creado es util para saber que tareas son realizadas por un usuario y a que paginas tiene acceso
                login(request, user)
                # return HttpResponse('<h1>user created successfully</h1>')
                return redirect ('tasks')
            # con solo declarando enfrente del except el error que queremos controlar podemos evitar que suceda
            except IntegrityError:
                return render(request, 'signup.html', {
                    'form':UserCreationForm,
                    'error':'User already exists'
                })    
        # return HttpResponse('Password do not match')
        return render(request, 'signup.html', {
            'form':UserCreationForm,
            'error':'password do not match'
        })



# tasks = funcion que lista las tareas que deben indicarse como completadas por cada usuario, es decir el valor de ("date_completed = null")
@login_required
def tasks(request):
    # Task.objects.all = muestra todas las tareas creadas por los usuarios
    # tasks = Task.objects.all()
    # filter = para mostrar las tareas que pertenecen al usuario actual usamos la propiedad user
    # aplicar otro tipos de filtros = filter puede recibir varios parametros para hacer un filtro mas completo, usamos como filtro las columnas de la tabla de nuestro modelo en este ejemolo "datcompleted" es una tabla del modelo TASK
    # datecompleted__isnull = True: muestra las tareas si la fecha de completado sea indicado
    tasks = Task.objects.filter(user = request.user, date_completed__isnull = True)
    return render(request, 'tasks.html', {'tasks':tasks})



# tasks_completed = funcion que lista las tareas completadas por cada usuario ("date_completed = timezone.now()")
@login_required
def tasks_completed(request):
    # .order_by('-date_completed') = ordena las tareas de mas reciente-antigua
    tasks = Task.objects.filter(user = request.user, date_completed__isnull = False).order_by('-date_completed')
    return render(request, 'tasks_complete.html', {'tasks':tasks})



# create_task = funcion que crea usuarios que han sido registrados e iniciado sesion
@login_required
def create_task(request):
    # GET = crea un query_set() vacio que almacenara la informacion que ingresa el usuario
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            # aqui renderizamos la clase TaskForm del archivo "forms.py"
            'form':TaskForm
        })
    else:
        try:
            # cuando presionamos el boton enviar del html create_task obtenemos la informacion del formulario y la mostramos en consola
            # POST = obtiene la informacion que ingresa el usuario al formulario y la guarda en el query_set() vacio
            # print(request.POST)
            # form = variable que crea el formulario
            form = TaskForm(request.POST)
            # new_task = variable que guarda los datos que hay en el formulario, commit nos permite evitar guardar los datos en la base, solo queremos obtenerlos para poder verlos, no necesitamos guardarlo
            new_task = form.save(commit=False)
            # con la propiedad user obtenemos el nombre del usuario que envia el formulario
            new_task.user = request.user
            # aqui guardamos los datos obtenidos del formulario
            new_task.save()
            # return render(request, 'create_task.html', {
            #     # aqui renderizamos el formulario personalizado y se mostrara en la tabla Task del admin
            #     'form':TaskForm
            # })
            return redirect ('tasks')
        # ValueError = lo utilizamos cuando queremos avisarle al usuario del programa que un dato o argumento que ingresó en la consola ha sido incorrecto
        except ValueError:
            return render(request, 'create_task.html', {
                # aqui renderizamos la clase TaskForm del archivo "forms.py"
                'form':TaskForm,
                'error':'Please provide valid data'
            })



# task_detail = funcion que obtiene las tareas creadas y las actualiza por medio de un formulario creado con forms.py
@login_required
def task_detail(request, task_id):
    # si el usuario hace una peticion por el metodo get entonces muestra el formulario de actualiacion
    if request.method == "GET":
        # get_object_or_404 = es otra de forma de obtener las tareas por medio de un id que ademas muestra un mensaje de error al cliente sin tener que tirar el servidor, alternativa a (objects.get(id = task_id))
            # Task = recibe como parametro el formulario que crear las tareas teniendo como referencia el id de cada tarea creada
            # id = parametro que indica el id de una tarea creada
            # user = muestra las tareas creadas por el usuario que ha iniciado sesion, esto funciona para evitar que otros usuarios no puedan modificar las tareas de otros
        task = get_object_or_404(Task, id = task_id, user = request.user)
        # instance = propiedad que crea un formulario apartir de la clase creada en el archivo "FORMS.PY"
        form = TaskForm(instance=task)
        return render(request, "task_detail.html", {'task':task, 'form':form})
    else:
        try:
            # 
            task = get_object_or_404(Task, id = task_id, user = request.user)
            form = TaskForm(request.POST, instance=task)
            form.save()
            return redirect('tasks')
        except ValueError:
            return render(request, "task_detail.html", {'task':task, 'form':form, 'error':'Error updating Task'})



# complete_task = funcion que cambia el valor del campo complete_task y si esta vacio le agrega un valor presionando el boton complete, el valor es la fecha actual
@login_required
def complete_task(request, task_id):
    # task = obtiene por medio de su id las tareas creadas por el usuario actual
    task = get_object_or_404(Task, id = task_id, user = request.user)
    # comprobamos si la respuesta es POST y si lo es entonces . . . 
    if request.method == 'POST':
        # agregamos el valor de fecha actual al campo date_complete del formulario de Task
        task.date_completed = timezone.now()
        # guardamos los cambios
        task.save()
        # redireccionamos al usuario a la vista "tasks"
        return redirect('tasks')



#delete_task = aplicacion que elimina las tareas registradas por un usuario logeado
@login_required
def delete_task(request, task_id):
    # task = obtiene por medio de su id las tareas creadas por el usuario actual
    task = get_object_or_404(Task, id = task_id, user = request.user)
    # comprobamos si la respuesta es POST y si lo es entonces . . . 
    if request.method == 'POST':            
        # eliminas la tarea creada por el usuario
        task.delete()
        # redireccionamos al usuario a la vista "tasks"
        return redirect('tasks')



# signout = funcion que cierra la sesion de un usuario
@login_required
def signout(request):
    # logout = elimina el cookie de la informacion de inicio de sesion del usuario activo
    logout(request)
    return redirect('home')



# signin = funcion que crea una sesion por usuario
def signin(request):
    # GET =  comprueba si se envian datos o si se esta recargando  la pagina
    if request.method == 'GET':
        return render(request, 'signin.html',{
            'form':AuthenticationForm
        })
    else:
        # podemos ver en consola la informacion que se recibe del form
        # print(request.POST)
        user = authenticate(request, username = request.POST['username'], password = request.POST['password'])
        if user is None:
            return render(request, 'signin.html', {'form':AuthenticationForm, 'error':'username or password is incorrrect'})
        else:
            login(request, user)
            return redirect('tasks')


