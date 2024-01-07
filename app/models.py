from django.db import models
from django.utils import timezone
# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    nascimento = models.DateField(null=False)
    peso = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    altura = models.IntegerField(null=False)
    imc = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return f'Pessoa [nome={self.nome}]'


class DiasTreino(models.Model):
    treino = models.BooleanField()
    registro = models.DateTimeField()

    def __str__(self):
        registro_local = timezone.localtime(self.registro)
        return f'DiasTreino [treino={self.treino}][registro={registro_local}]'