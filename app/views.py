from django.shortcuts import render
from app.models import DiasTreino
from app.calendario import Calendario
from datetime import datetime


# class Usuario:

#     ano_atual = datetime.now().year
#     idade = 0

#     def __init__(self, nome, nascimento, peso, altura, imc):
#         self.nome = nome
#         self.nascimento = nascimento
#         self.peso = peso
#         self.altura = altura
#         self.imc = imc

def index(request):

    meu_calendario = Calendario()
    datas = meu_calendario.calendario()

    treinos = DiasTreino.objects.all()
    ultimo_registro = treinos.last()

    dias_treinados = DiasTreino.objects.filter(treino=True)

    qtd_treinos = len(dias_treinados)

    if request.method == 'POST':
        escolha = request.POST.get('botao')

        if ultimo_registro is not None:

            if ultimo_registro.registro.day != datetime.now().day:

                if escolha == 'sim':
                    dia_treino = DiasTreino(treino=True)
                else:
                    dia_treino = DiasTreino(treino=False)
                
                dia_treino.save()
        
        else:
            if escolha == 'sim':
                dia_treino = DiasTreino(treino=True)
            else:
                dia_treino = DiasTreino(treino=False)
        
            dia_treino.save()


    return render(request, 'index.html', {'datas': datas, 'treinos': treinos, 'qtd_treinos': qtd_treinos})

