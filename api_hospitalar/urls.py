
from rest_framework.routers import SimpleRouter
from api_hospitalar.views import MedicosAPI, PacientesAPI, ConsultasAPI

# gerador de rotas do Rest
router = SimpleRouter()
router.register('medicos', MedicosAPI)
router.register('pacientes', PacientesAPI)
router.register('consultas', ConsultasAPI)
