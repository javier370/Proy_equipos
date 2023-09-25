from django.contrib import admin
from tarea.models import Tarea

@admin.register(Tarea)
class TareaAdmin(admin.ModelAdmin):
    pass
