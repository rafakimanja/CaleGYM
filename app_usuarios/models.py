from django.db import models


class Usuario(models.Model):
    nome_usuario = models.CharField(max_length=100, null=False)
    senha = models.CharField(max_length=25, null=False)
    peso = models.DecimalField(max_digits=5, decimal_places=2, null=False)
    altura = models.IntegerField(null=False)
    imc = models.DecimalField(max_digits=3, decimal_places=1, default=0.0)

    def __str__(self):
        return f'[{self.id}] {self.nome_usuario}'
