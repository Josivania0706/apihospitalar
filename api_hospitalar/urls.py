
from rest_framework.routers import SimpleRouter
from api_hospitalar.views import *

# gerador de rotas do Rest
router = SimpleRouter()
router.register('medicos', Medicos_API)
router.register('pacientes', Pacientes_API)
router.register('consultas', Consultas_API)
