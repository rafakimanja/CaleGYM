from django.db import models

# Create your models here.

class Pessoa(models.Model):
    nome = models.CharField(max_length=100, null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    senha = models.CharField(max_length=20, null=False, blank=False)
    nascimento = models.DateField(null=False)
    peso = models.DecimalField(max_digits=4, decimal_places=2, null=False)
    altura = models.IntegerField(null=False)
    imc = models.DecimalField(max_digits=2, decimal_places=1, default=0)

    def __str__(self):
        return f'Pessoa [nome={self.nome}]'

    # def calcula_imc(self):
    #    return self.peso / (self.altura ** 2)
    
    # @property
    # def imc(self):
    #     return self.imc
    
    # @imc.setter
    # def imc(self):
    #     if self.imc == 0:
    #         self.imc = self.calcula_imc()