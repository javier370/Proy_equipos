from django.db import models
from tarea.models import Tarea
from equipo.models import User_equipo

class Tarea_asignada(models.Model):
    tarea = models.ForeignKey(Tarea, on_delete=models.CASCADE)
    user_equipo = models.ForeignKey(User_equipo, on_delete=models.CASCADE)
    estado = models.CharField(max_length=50, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.tarea} - {self.user_equipo} - {self.estado}'
    
    class Meta:
        db_table = 'tarea_asignada'
