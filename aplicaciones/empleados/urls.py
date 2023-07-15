from django.urls import path,include
from aplicaciones.empleados.views import EmpleadosListView,EmpleadoDetallado,AdministrarEmpleado,EditarEmpleado,EliminarEmpleado,CrearEmpleado
app_name = 'empleado_app'
urlpatterns = [
    path('',EmpleadosListView.as_view(), name = "generico"),
    path('detallado/<pk>/',EmpleadoDetallado.as_view(), name = "Detallado"),
    path('administrar/',AdministrarEmpleado.as_view(), name = "administrar"),
    path('editar/<pk>/',EditarEmpleado.as_view(), name = "editar"),
    path('eliminar/<pk>/',EliminarEmpleado.as_view(),name = "eliminar"),
    path('registrar/',CrearEmpleado.as_view(),name = "registrar")
]
