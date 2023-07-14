from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import Empleado
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
    
# Create your views here.
