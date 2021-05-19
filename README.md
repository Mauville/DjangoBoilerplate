# Django Tests
Register Students with a REST API using Django.

Unit, integration, automated and functionality test were performed. 

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

## Run automated tests
```
npm i
npx cypress open
```
