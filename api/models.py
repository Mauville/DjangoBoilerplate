import datetime
from django.db import models
from django.core.exceptions import ValidationError


class Estudiante(models.Model):
    nombres = models.CharField(max_length=100, null=False)
    apellidos = models.CharField(max_length=100, null=False)
    ciudad = models.CharField(max_length=100, null=False)
    fecha_nacimiento = models.DateField(null=False)
