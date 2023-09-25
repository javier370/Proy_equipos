from django.db import models
from user.models import User


class Equipo(models.Model):
    nombre = models.CharField(max_length=50, null=False, blank=False, unique=True)

    def __str__(self):
        return f'{self.nombre}'
    
class User_equipo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    equipo = models.ForeignKey(Equipo, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} - {self.equipo}'
    
    class Meta:
        db_table : 'user_equipo'
