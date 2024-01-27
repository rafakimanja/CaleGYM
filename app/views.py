from django.shortcuts import render, redirect
from django.contrib import messages
from app.models import DiasTreino
from app.calendario import Calendario
from app_usuarios.models import Usuario
from datetime import datetime


def home(request):

    # minhas classe de calendário
    meu_calendario = Calendario()
    datas = meu_calendario.calendario()

    # variáveis de sessão
    id_usuario = request.session.get('id_usuario', None)

    # objeto usuário
    usuario_obj = Usuario.objects.get(pk=id_usuario)

    # dados banco de dados
    treinos = DiasTreino.objects.filter(usuario=id_usuario)
    ultimo_registro = treinos.last()

    dias_treinados = DiasTreino.objects.filter(usuario=id_usuario, treino=True)
    qtd_treinos = len(dias_treinados)
    ultimo_treino = dias_treinados.last()

    if request.method == 'POST':
        escolha = request.POST.get('botao')

        if ultimo_registro.registro.day != datetime.now().day:

            if escolha == 'sim':
                dia_treino = DiasTreino(treino=True, usuario=usuario_obj)
            else:
                dia_treino = DiasTreino(treino=False, usuario=usuario_obj)
            
            dia_treino.save()
        
        else:
            messages.error(request, 'Não é possível registrar mais de 1 treino por dia!')
        
        return redirect('home')
    
    return render(request, 'app/home.html', {'datas': datas, 'treinos': treinos, 'qtd_treinos': qtd_treinos, 'usuario_obj': usuario_obj, 'ultimo_treino': ultimo_treino.registro.date})

