from api_hospitalar.models import *
from rest_framework import viewsets
from api_hospitalar.serializers import *
from api_hospitalar.permissions import *

# Create your views here.

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

class Consultas_API(viewsets.ModelViewSet):
    """ API para gerenciamento de consultas."""
    queryset = Consulta.objects.all()
    serializer_class = Consulta_Serializer
    permission_classes = [User_Permissions]