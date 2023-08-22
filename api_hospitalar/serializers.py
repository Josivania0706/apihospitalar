from api_hospitalar.models import *
from rest_framework import serializers

'Os campos mostrados nas classes serializers são o que apareceram no Rest'

class Medico_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Medico
        fields = ['id', 'nome', 'especializacao', 'crm']

class Paciente_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = ['id', 'nome', 'idade', 'cidade']

class Consulta_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Consulta
        fields = ['id', 'paciente', 'medico', 'data_consulta']

