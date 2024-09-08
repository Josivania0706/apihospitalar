from api_hospitalar.models import *
from rest_framework import serializers
from django.contrib.auth import get_user_model

'Os campos mostrados nas classes serializers são o que apareceram no Rest'

class MedicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'idade', 'sexo', 'cidade', 'especializacao', 'crm']

class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'idade', 'sexo', 'cidade']

class ConsultaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'paciente', 'medico', 'diagnostico', 'prescricao', 'data_consulta']
