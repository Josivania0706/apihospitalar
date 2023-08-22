
from django.contrib import admin
from django.urls import path, include
from api_hospitalar.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')), # pagina de login do rest
]
