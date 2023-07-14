from django.contrib import admin
from .models import *
admin.site.register(Habilidades)

class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('nombre_empleado','apellido_empleado','departamento','trabajo_empleado')
    search_fields = ('nombre_empleado',)
    list_filter = ('trabajo_empleado',)

admin.site.register(Empleado,EmpleadoAdmin)
# Register your models here.
