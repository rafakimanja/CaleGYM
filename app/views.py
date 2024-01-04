from django.shortcuts import render
from app.models import Pessoa
from datetime import datetime

class Usuario:

    ano_atual = datetime.now().year
    idade = 0

    def __init__(self, nome, nascimento, peso, altura, imc):
        self.nome = nome
        self.nascimento = nascimento
        self.peso = peso
        self.altura = altura
        self.imc = imc
    
    @classmethod
    def calcula_idade(cls, self):
        cls.idade = cls.ano_atual - self.nascimento
    
    def calcula_imc(self):
       return self.peso / (self.altura ** 2)
    
    @property
    def imc(self):
        return self.imc
    
    @imc.setter
    def imc(self):
        if self.imc == 0:
            self.imc = self.calcula_imc()

        

def index(request):
    return render(request, 'index.html')


def cadastro(request):

    