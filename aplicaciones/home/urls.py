from django.urls import path,include
from .views import vistaInicial
urlpatterns = [
    path('',vistaInicial.as_view()),
    path('empleados/',include('aplicaciones.empleados.urls')),
    path('departamento/',include('aplicaciones.departamento.urls'))
]
