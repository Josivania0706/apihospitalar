from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from api_hospitalar.models import Medico, Paciente, Consulta
from api_hospitalar.serializers import MedicoSerializer, PacienteSerializer, ConsultaSerializer
from api_hospitalar.permissions import User_Permissions
from datetime import datetime
from rest_framework.decorators import action


class MedicosAPI(viewsets.ModelViewSet):
    """ API para gerenciamento de médicos."""

    queryset = Medico.objects.all()
    serializer_class = MedicoSerializer
    permission_classes = [User_Permissions]

    @action(detail=True, methods=['patch'], url_path='arquivar')
    def arquivar(self, request, pk=None):
        medico = self.get_object()
        medico.status = 'arquivado'  # RF008
        medico.save()
        return Response({'status': 'medico arquivado'})


class PacientesAPI(viewsets.ModelViewSet):
    """ API para gerenciamento de pacientes."""

    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer
    permission_classes = [User_Permissions]

    @action(detail=True, methods=['patch'], url_path='arquivar')
    def arquivar(self, request, pk=None):
        paciente = self.get_object()
        paciente.status = 'arquivado'  # RF012
        paciente.save()
        return Response({'status': 'paciente arquivado'})

    @action(detail=True, methods=['get'])
    def consultas(self, request, pk=None):
        paciente = self.get_object()
        consultas = Consulta.objects.filter(paciente=paciente)
        serializer = ConsultaSerializer(consultas, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'], url_path='consultas/') #RF22
    def relatorio_diario_retornos(self, request):
        """ Gera um relatório diário com os retornos de pacientes. """
        hoje = datetime.now().date()
        consultas_hoje = Consulta.objects.filter(data_consulta__date=hoje)
        serializer = ConsultaSerializer(consultas_hoje, many=True)
        return Response(serializer.data)


class ConsultasAPI(viewsets.ModelViewSet):
    """ API para gerenciamento de consultas."""

    queryset = Consulta.objects.all()
    serializer_class = ConsultaSerializer
    permission_classes = [User_Permissions]

    @action(detail=True, methods=['patch'], url_path='arquivar')
    def arquivar(self, request, pk=None):
        consulta = self.get_object()
        consulta.status = 'arquivada'  # RF016
        consulta.save()
        return Response({'status': 'consulta arquivada'})
    
    @action(detail=False, methods=['get'], url_path='historico')   #RF28
    def historico_consultas(self, request):
        data_inicio = request.query_params.get('data_inicio')
        data_fim = request.query_params.get('data_fim')
        if data_inicio and data_fim:
            consultas = Consulta.objects.filter(data_consulta__range=[data_inicio, data_fim])
            serializer = ConsultaSerializer(consultas, many=True)
            return Response(serializer.data)
        return Response({"error": "Datas inválidas ou ausentes"}, status=400)


