from django.shortcuts import render
from django.views.generic import TemplateView

class vistaInicial(TemplateView):
    template_name = "home/inicio.html"
# Create your views here.
