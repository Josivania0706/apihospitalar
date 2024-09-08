from rest_framework.permissions import BasePermission

class UserPermissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Atendentes').exists():
            return request.method in ['GET', 'POST', 'PUT', 'DELETE']  # Permissão completa para Atendentes (RF001)
        
        elif request.user.groups.filter(name='Medicos').exists():
            return request.method in ['GET', 'PUT']  # Médicos podem visualizar (RF009)

        elif request.user.groups.filter(name='Leitores').exists():
            if request.method == 'POST' and view.basename == 'consultas':  # Leitor pode agendar consultas (RF025)
                return True
            return request.method in ['GET']  # Leitores só podem visualizar
        
        return False
