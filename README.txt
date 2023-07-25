Para iniciar un proyecto de django es buena practica crear el proyecto dentro de un ambiente virtual para comtrolar las actualizaciones de las librerias y administrarlas, tambien sirve para aislar los proyectos y manejar las versiones del mismo

-- este proyecto puede manejar el inicio de sesion y administra una base de datos en POSTGRESQL

-- el entorno virtual que se utiliza es con el modulo "VENV"

    INSTRUCCION EN CONSOLA: indica que se crea una carpeta llamada venv con el modulo VENV 

------- py -m venv venv

            donde:
                py = abreviacion de python
                -m = indicamos que hacemos uso de un modulo
                venv = nombre del modulo que utilizaremos, en este caso este modulo crea un entorno virtual
                venv = nombre de la carpeta que contendra el entorno virtual

-- una vez ejecutada la instruccion se creara la carpeta y "VENV" para activar el entorno virtual debes presionar "fn + f1" para seleccionar el interprete de python y ahi aparecera el entorno virtual venv algo parecido a "(BASE) DE CONDA"

-- ahora ya podemos instalar las librerias necesarias para nuestro proyecto como django,

-- una buena practica es agregar la propiedad "NAME" en el url de las apps creadas en el archivo "urls.py" de la carpeta principal del proyecto

-- la carpeta "STATIC" recibe los archivos estaticos del proyecto ("html, jsvascript, imagenes")

-- en el archivo settings en la parte de "DATABASES" agregamos la base de datos que deseemos para nuestro proyecto

-- Estructura de una app de django, ¿para que sirven los archivos de una app?

    -- carpeta migrations: guarda las migraciones o cambios realizados en el proyecto especialmente en el archivo models.py
    -- archivo admin.py: con este archivo añadimos los modelos a el panel de administrador, podemos dar permisos de administrador a diferentes usuarios
    -- archivo apps.py: archivo que maneja las configuraciones de una app
    -- archivo models.py: archivo que crea las tablas y columnas sql con codigo python
    -- archivo texts.py: archivo que comprueba si se ejecuta bien el codigo, (explicacion fuera de este curso)
    -- archivo views.py: archivo que crea funciones con mensajes o objetos que retorna el navegador, renderiza html como mensaje

-- django tiene modulos ORM que permiten hacer CRUD de SQL con codigo PYTHON

    -- models = es el ORM que utilizamos en este proyecto web

-- IMPORTANTE: "SELF" es una referencia que tiene el modelo hacia el mismo "(¿self = modelo?)"

-- GUARDAR TAREAS: podemos guardarlos de varias formas por ejemplo usando el archivo forms.py para utilizar como almacen de informacion

-- PROTEGER RUTAS URL: esta propiedad se indica en el archivo settings.py de un proyectoweb django

    -- LOGIN_URL = propiedad que indica en que ruta se encuentra el inicio de sesion de un usuario registrado    
        -- esta propiedad nos ayuda a proteger las rutas url ya que is un usuario desea ingresar a una pagina que regquiere login, sera redireccionado a "/signin" o inicio de sesion
        -- LOGIN_URL = '/signin'

-- BOOTSTRAP: agregar estilos y personalizar el proyectoweb terminado

    -- CDN links =  para utilizar bootsrap necesitamos agregar un link en el header del archivo base de nuestro proyectoweb
    -- abre la pagina de https://getbootstrap.com/docs/5.3/getting-started/introduction/ seccion CDN links
        
        https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css
    
    -- ingresar a bootstrap es esencial para comprender como estilizar una pagina web es muy importante ingresar y leer la documentacion del framework bootstrap

        -- ejemplo de codigo: como hacer responsive un navbar

                <nav class="navbar navbar-expand-lg bg-body-tertiary">
                    <div class="container-fluid">
                        <a class="navbar-brand" href="#">Navbar</a>
                        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNav"
                            aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
                            <span class="navbar-toggler-icon"></span>
                        </button>
                        <div class="collapse navbar-collapse" id="navbarNav">
                            # aqui agregamos los elementos al navbar en un ul que contengan li
                        </div>
                    </div>
                </nav>