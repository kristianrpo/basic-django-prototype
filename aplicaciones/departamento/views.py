from django.shortcuts import render
from django.views.generic import ListView
from .models import Departamento
from aplicaciones.empleados.models import Empleado
class DepartamentoListView(ListView):
    model = Departamento
    template_name = "departamento/listar_departamentos.html"
    context_object_name = "departamento"

class FiltrarEmpleados(ListView):
    model = Empleado
    template_name = "empleados/empleados.html"
    context_object_name = "empleado"
    def get_queryset(self):
        nombre_corto_1 = self.kwargs['nombre_corto']
        lista = Empleado.objects.filter(departamento__nombre_corto_departamento=nombre_corto_1)
        return lista

