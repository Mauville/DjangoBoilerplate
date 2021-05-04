# Pruebas en DJANGO
Projecto en DJANGO REST FRAMEWORK para hacer un registro de alumnos con front en HTML que accede a una REST API en Django.

Se realizaron pruebas de unidad, integracion y de funcionalidad.

## Setup
```
Inicializar el venv.
pip install django
pip install django-cors-headers
pip install djangorestframework
```

## Levantar server
```
python3 manage.py runserver
```
La pagina de registro se accede en [localhost:8000](http://localhost:8000)

Los endpoints se acceden en [/api/estudiantes/](http://localhost:8000/api/estudiantes/)

## Correr tests
```
python3 manage.py test -v 2
```
