from django.db import models

# Create your models here.
from django.db import models

# Classe abstrata
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1)
    cidade = models.CharField(max_length=200)
    
class Paciente(Pessoa):
    procedimento_medico = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Medico(Pessoa):
    especializacao = models.CharField(max_length=200)
    crm = models.CharField(max_length=200)

    def __str__(self):
        return self.nome


class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING)
    data_consulta = models.DateTimeField(auto_now_add=True)
    diagnostico = models.CharField(max_length=400)
    prescricao = models.CharField(max_length=500)

    def __str__(self):
        return f'{self.id} - {self.paciente} - {self.medico}'

