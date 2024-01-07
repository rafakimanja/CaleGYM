from django.shortcuts import render
from app.models import Pessoa, DiasTreino
from datetime import datetime
from django.utils import timezone

class Usuario:

    ano_atual = datetime.now().year
    idade = 0

    def __init__(self, nome, nascimento, peso, altura, imc):
        self.nome = nome
        self.nascimento = nascimento
        self.peso = peso
        self.altura = altura
        self.imc = imc
    

        

def index(request):

    dia = datetime.now().date
    semana = dia_semana(datetime.now().weekday()) 
    

    data = {
        'dia': dia,
        'semana': semana
    }

    contador = request.session.get('qtd', 0)

    if request.method == 'POST':
        escolha = request.POST.get('botao')

        if escolha == 'sim':
            dia_treino = DiasTreino(treino=True, registro=timezone.now())
            dia_treino.save()
        
        else:
            dia_treino = DiasTreino(treino=False, registro=timezone.now())
            dia_treino.save()
            
    treinos = DiasTreino.objects.all()

    return render(request, 'index.html', {'data': data, 'treinos': treinos})



def dia_semana(dia):
    
    match dia:

        case 0:
            return 'Segunda-Feira'
        
        case 1:
            return 'Terça-Feira'
        
        case 2:
            return 'Quarta-Feira'
        
        case 3:
            return 'Quinta-Feira'
        
        case 4:
            return 'Sexta-Feira'
        
        case 5:
            return 'Sábado'
        
        case 6:
            return 'Domingo'