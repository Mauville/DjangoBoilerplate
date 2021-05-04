from api.models import Estudiante
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from api.serializers import EstudianteSerializer


class EstudianteViewSet(ModelViewSet):
    """
    API endpoint that allows students to be viewed or edited.
    """
    queryset = Estudiante.objects.all().order_by('-nombres')
    serializer_class = EstudianteSerializer
    permission_classes = [permissions.AllowAny]
