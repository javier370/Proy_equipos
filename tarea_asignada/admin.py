from django.contrib import admin
from tarea_asignada.models import Tarea_asignada

@admin.register(Tarea_asignada)
class TareaAsignadaAdmin(admin.ModelAdmin):
    pass
