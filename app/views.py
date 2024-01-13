from django.shortcuts import render
from app.models import DiasTreino
from app.calendario import Calendario
from datetime import datetime


def home(request):

    #minhas classe de calendário
    meu_calendario = Calendario()
    datas = meu_calendario.calendario()

    # variáveis de sessão
    id_usuario = request.session.get('id_usuario', None)

    #dados banco de dados
    treinos = DiasTreino.objects.filter(usuario=id_usuario)
    ultimo_registro = treinos.last()

    dias_treinados = DiasTreino.objects.filter(usuario=id_usuario, treino=True)
    qtd_treinos = len(dias_treinados)

    if request.method == 'POST':
        escolha = request.POST.get('botao')

        if ultimo_registro is not None:

            if ultimo_registro.registro.day != datetime.now().day:

                if escolha == 'sim':
                    dia_treino = DiasTreino(treino=True, usuario=id_usuario)
                else:
                    dia_treino = DiasTreino(treino=False, usuario=id_usuario)
                
                dia_treino.save()
        
        else:
            if escolha == 'sim':
                dia_treino = DiasTreino(treino=True)
            else:
                dia_treino = DiasTreino(treino=False)
        
            dia_treino.save()

    return render(request, 'app/home.html', {'datas': datas, 'treinos': treinos, 'qtd_treinos': qtd_treinos})

