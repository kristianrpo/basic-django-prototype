from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView,DeleteView,UpdateView
from .models import Empleado
from django.urls import reverse_lazy
class EmpleadosListView(ListView):
    model = Empleado
    template_name = "empleados/empleados.html"
    paginate_by = 6
    context_object_name = "empleado"
    def get_queryset(self):
        palabra_clave = self.request.GET.get("nombre",'')
        lista = Empleado.objects.filter(nombre_empleado__icontains = palabra_clave)
        if len(lista)>0:
            return lista
        else:
            return super().get_queryset()
        
class EmpleadoDetallado(DetailView):
    model = Empleado
    template_name = "empleados/empleado_detallado.html"
    context_object_name = "empleado"
    
class AdministrarEmpleado(ListView):
    model = Empleado
    template_name = "empleados/administrar.html"
    paginate_by = 6
    context_object_name = "empleado"

class EditarEmpleado(UpdateView):
    model = Empleado
    template_name = "empleados/editar.html"
    fields = ('__all__')
    success_url = reverse_lazy('empleado_app:generico')
    context_object_name = "empleado"

class EliminarEmpleado(DeleteView):
    model = Empleado
    template_name = "empleados/administrar.html"
# Create your views here.
