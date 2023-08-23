from api_hospitalar.models import *
from api_hospitalar.serializers import *
from api_hospitalar.permissions import *
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response



class Medicos_API(viewsets.ModelViewSet):
    """ API para gerenciamento de médicos."""

    queryset = Medico.objects.all()
    serializer_class = Medico_Serializer
    permission_classes = [User_Permissions]


class Pacientes_API(viewsets.ModelViewSet):
    """ API para gerenciamento de pacientes."""

    queryset = Paciente.objects.all()
    serializer_class = Paciente_Serializer
    permission_classes = [User_Permissions]

    @action(detail=True, methods=['get'])
    def consultas(self, request, pk=None):
        paciente = self.get_object()
        consultas = Consulta.objects.filter(paciente=paciente)
        serializer = Consulta_Serializer(consultas, many=True)
        return Response(serializer.data)


class Consultas_API(viewsets.ModelViewSet):
    """ API para gerenciamento de consultas."""

    queryset = Consulta.objects.all()
    serializer_class = Consulta_Serializer
    permission_classes = [User_Permissions]
