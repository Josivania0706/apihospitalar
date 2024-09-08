from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from datetime import timedelta


# Classe abstrata
class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    idade = models.PositiveIntegerField()
    sexo = models.CharField(max_length=1)
    cidade = models.CharField(max_length=200)
    data_criacao = models.DateTimeField(auto_now_add=True)  # RF003
    ultimo_login = models.DateTimeField(null=True, blank=True)  # RF004

class Paciente(Pessoa):
    procedimento_medico = models.CharField(max_length=200)
    status = models.CharField(max_length=10, default='ativo')  # RF012

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

class Medico(Pessoa):
    especializacao = models.CharField(max_length=200)
    crm = models.CharField(max_length=200)
    status = models.CharField(max_length=10, default='ativo')  # RF008

    def __str__(self):
        return self.nome

    class Meta:
        ordering = ['nome']

    def save(self, *args, **kwargs):            #RF27
        super(Consulta, self).save(*args, **kwargs)
        # Notificar o Leitor um dia antes da consulta
        if self.paciente.groups.filter(name='Leitores').exists():
            envio_notificacao = self.data_consulta - timedelta(days=1)
            send_mail(
                'Lembrete de Consulta',
                f'Você tem uma consulta agendada com {self.medico.nome} no dia {self.data_consulta}.', {self.paciente.email},
                [self.paciente.email],
                eta=envio_notificacao,
                fail_silently=False,
            )
    
    

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.DO_NOTHING)
    medico = models.ForeignKey(Medico, on_delete=models.DO_NOTHING)
    data_consulta = models.DateTimeField(auto_now_add=True)
    diagnostico = models.CharField(max_length=400)
    prescricao = models.CharField(max_length=500)
    status = models.CharField(max_length=10, default='ativa')  # RF016

    def __str__(self):
        return f'{self.id} - {self.paciente} - {self.medico}'

    class Meta:
        ordering = ['paciente']

class Usuario(AbstractBaseUser):                 #RF24
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=128)  
    
    def save(self, *args, **kwargs):
        if self.password and not self.password.startswith('pbkdf2_'): 
            self.password = make_password(self.password)
        super(Usuario, self).save(*args, **kwargs)