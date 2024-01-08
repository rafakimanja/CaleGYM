from django.shortcuts import render
from app.models import DiasTreino
from django.utils import timezone
from app.calendario import Calendario


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

    if request.method == 'POST':
        escolha = request.POST.get('botao')

        if escolha == 'sim':
            dia_treino = DiasTreino(treino=True)
            dia_treino.save()
        
        else:
            dia_treino = DiasTreino(treino=False)
            dia_treino.save()

    return render(request, 'index.html', {'datas': datas, 'treinos': treinos})