import datetime
import sqlite3

from django.db import utils
from django.test import TestCase
from django.utils import timezone
from rest_framework.test import APIRequestFactory

from api.models import Estudiante
from api.serializers import EstudianteSerializer
from api.viewsets import EstudianteViewSet


class EstudianteUnitTests(TestCase):
    def test_create_empty(self):
        try:
            Estudiante.objects.create()
        except:
            self.assertRaises(utils.IntegrityError)

    def test_create_estudiante_all_null(self):
        try:
            estudiante = Estudiante.objects.create(
                nombres=None,
                apellidos=None,
                ciudad=None,
                fecha_nacimiento=None
            )
        except:
            self.assertRaises(utils.IntegrityError)

    def test_create_estudiante_default(self):
        today = datetime.date.today()
        estudiante = Estudiante.objects.create(
            nombres='Juan',
            apellidos='Perez',
            ciudad='CDMX',
            fecha_nacimiento=today
        )
        self.assertIs(estudiante.nombres, 'Juan')
        self.assertIs(estudiante.apellidos, 'Perez')
        self.assertIs(estudiante.ciudad, 'CDMX')
        self.assertIs(estudiante.fecha_nacimiento, today)

    def test_create_estudiante_overage(self):
        today = datetime.datetime(2000, 1, 1)
        estudiante = Estudiante.objects.create(
            nombres='Juan',
            apellidos='Perez',
            ciudad='CDMX',
            fecha_nacimiento=today
        )
        serializer = EstudianteSerializer(data=estudiante.__dict__)
        self.assertIs(serializer.is_valid(), False)


class EstudianteIntegrationTests(TestCase):
    def setUp(self):
        Estudiante.objects.create(
            nombres='Juan',
            apellidos='Perez',
            ciudad='CDMX',
            fecha_nacimiento=datetime.date.today()
        )
        Estudiante.objects.create(
            nombres='Roberto',
            apellidos='Juárez',
            ciudad='CDMX',
            fecha_nacimiento=datetime.date(2000, 1, 1)
        )

    def test_delete_estudiante_default(self):
        estudiante = Estudiante.objects.get(nombres='Juan')
        request = APIRequestFactory().delete('/api/estudiantes/')
        data = {'delete': 'destroy'}
        estudiantes = EstudianteViewSet.as_view(data)
        response = estudiantes(request, pk=estudiante.id)
        self.assertEqual(response.status_code, 204)

    def test_get_estudiantes(self):
        request = APIRequestFactory().get("/api/estudiantes/")
        data = {'get': 'list'}
        estudiantes = EstudianteViewSet.as_view(data)
        response = estudiantes(request)
        self.assertEqual(response.status_code, 200)

    def test_get_estudiante_default(self):
        estudiante = Estudiante.objects.get(nombres='Juan')
        request = APIRequestFactory().get('/api/estudiantes/')
        data = {'get': 'retrieve'}
        estudiantes = EstudianteViewSet.as_view(data)
        response = estudiantes(request, pk=estudiante.id)
        self.assertEqual(response.status_code, 200)

    def test_get_estudiante_not_found(self):
        request = APIRequestFactory().get('/api/estudiantes/')
        data = {'get': 'retrieve'}
        estudiantes = EstudianteViewSet.as_view(data)
        response = estudiantes(request, pk=-1)
        self.assertEqual(response.status_code, 404)

    def test_post_estudiante_default(self):
        estudiante = Estudiante.objects.get(nombres='Juan')
        request = APIRequestFactory().post('/api/estudiantes/', estudiante.__dict__)
        data = {'post': 'create'}
        estudiantes = EstudianteViewSet.as_view(data)
        response = estudiantes(request)
        self.assertEqual(response.status_code, 201)

    def test_post_estudiante_overage(self):
        estudiante = Estudiante.objects.get(nombres='Roberto')
        request = APIRequestFactory().post('/api/estudiantes/', estudiante.__dict__)
        data = {'post': 'create'}
        estudiantes = EstudianteViewSet.as_view(data)
        response = estudiantes(request)
        self.assertEqual(response.status_code, 400)
