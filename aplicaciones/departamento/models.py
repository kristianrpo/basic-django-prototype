from django.db import models
class Departamento (models.Model):
    nombre_departamento = models.CharField(("Nombre"), max_length=50, blank = True)
    nombre_corto_departamento = models.CharField(("Psudonimo"), max_length=20)
    activo_departamento = models.BooleanField(("False"),default = False)
    def __str__(self):
        return str(self.id)+"-"+self.nombre_departamento
# Create your models here.
