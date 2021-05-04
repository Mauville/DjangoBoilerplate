from rest_framework import serializers
from api.models import Estudiante
import datetime


class EstudianteSerializer(serializers.HyperlinkedModelSerializer):
    # id = serializers.ReadOnlyField()

    class Meta:
        model = Estudiante
        fields = ('id', 'nombres', 'apellidos', 'ciudad', 'fecha_nacimiento')

    def validate(self, data):
        """
        Check that the start is before the stop.
        """
        year = datetime.date.today().year - 18
        month = datetime.date.today().month
        day = datetime.date.today().day
        if data['fecha_nacimiento'] and data['fecha_nacimiento'] < datetime.date(year, month, day):
            raise serializers.ValidationError(
                {"fecha_nacimiento": "El estudiante debe ser menor de 18 años."}
            )
        return data
