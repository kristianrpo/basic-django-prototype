from django.db import models
from aplicaciones.departamento.models import Departamento

class Habilidades(models.Model):
    habilidad = models.CharField(("Habilidad"), max_length=50)
    def __str__(self):
        return str(self.id)+"-"+self.habilidad
class Empleado (models.Model):
    opciones_trabajo = (('0','Contador'),('1','Cantante'),('2','Ecologa'),('3','Futbolista'))
    nombre_empleado = models.CharField(("Nombres"), max_length=60)
    apellido_empleado = models.CharField(("Apellidos"), max_length=60)
    trabajo_empleado = models.CharField(("Empleo"), max_length=100, choices = opciones_trabajo)
    departamento = models.ForeignKey((Departamento), on_delete = models.CASCADE)
    habilidad = models.ManyToManyField((Habilidades))
    nombre_completo_mpleado = models.CharField(("Nombre Completo"), max_length=120, blank = True)
    def __str__(self):
        return str(self.id)+"-"+self.nombre_empleado
# Create your models here.
