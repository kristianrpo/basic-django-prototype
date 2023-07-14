from django.urls import path,include
from aplicaciones.departamento.views import DepartamentoListView, FiltrarEmpleados
app_name = 'departamento_app'
urlpatterns = [
    path('',DepartamentoListView.as_view()),
    path('filtrar_empleados/<nombre_corto>/',FiltrarEmpleados.as_view(), name = "filtro")
]