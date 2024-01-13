from django.db import models
from datetime import datetime, timedelta
from app_usuarios.models import Usuario

class DiasTreino(models.Model):
    treino = models.BooleanField()
    registro = models.DateTimeField(default=(datetime.now() - timedelta(hours=3)))
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'DiasTreino treino={self.treino} [data={self.registro}]'
