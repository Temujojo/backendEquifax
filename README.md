# BackendEquifax

## Requisitos
- python [link](https://www.python.org/downloads/)
- django [link](https://www.djangoproject.com/download/)

## Pasos a seguir

1. instalar Python 
2. cloar repositorio
3. desde la consola, en directorio `backendEquifax` ejecutar `python -m pip install django-cors-headers`, para permitir el uso de la api en el frontend
4. ejecutar en consola `python manage.py runserver 127.0.0.1:8000`, la consola debería mostrar lo siguiente.
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
May 20, 2024 - 03:47:54
Django version 5.0.6, using settings 'backendEquifax.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
5. ahora puede consumir la los endpoints desde frontendEquifax [Link](https://github.com/Temujojo/frontendEquifax)
