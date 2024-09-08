from django.contrib import admin

from api_hospitalar.models import Medico, Paciente, Consulta
# Register your models here.
class MedicoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'especializacao', 'crm']
    ordering = ['nome',]

class PacienteAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'idade', 'cidade']
    ordering = ['nome',]

class ConsultaAdmin(admin.ModelAdmin):
    list_display = ['id', 'paciente', 'medico', 'data_consulta']
    ordering = ['data_consulta',]

# register in django admin
admin.site.register(Medico, MedicoAdmin)
admin.site.register(Paciente, PacienteAdmin)
admin.site.register(Consulta, ConsultaAdmin)

