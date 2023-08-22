from  rest_framework.permissions import BasePermission

class User_Permissions(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='Atendentes').exists():
            return request.method in ['GET', 'POST', 'PUT']
        
        elif request.user.groups.filter(name='Medicos').exists():
            return request.method in ['GET', 'POST', 'PUT', 'DELETE']
        
        elif request.user.groups.filter(name='Leitores').exists():
            return request.method in ['GET']
        
        return False
        
        



