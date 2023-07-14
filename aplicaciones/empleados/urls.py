from django.urls import path,include
from aplicaciones.empleados.views import EmpleadosListView,EmpleadoDetallado
app_name = 'empleado_app'
urlpatterns = [
    path('',EmpleadosListView.as_view()),
    path('<pk>/',EmpleadoDetallado.as_view(), name = "Detallado"),
]
