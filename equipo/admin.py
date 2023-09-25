from django.contrib import admin
from equipo.models import Equipo, User_equipo

@admin.register(Equipo)
class EquipoAdmin(admin.ModelAdmin):
    pass

@admin.register(User_equipo)
class UserEquipoAdmin(admin.ModelAdmin):
    pass
