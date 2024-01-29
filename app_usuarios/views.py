from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForms, LoginForms, UsuarioForms
from .models import Usuario, PesoUsuario
from .authenticate import Autenticacao
import random


def index(request):

    autentic = Autenticacao()

    if not autentic.verifica_sessao(request):
        messages.error(request, 'Você não esta logado')
        return render(request, 'app_usuarios/index.html')
    else:
        return redirect('home')


def login(request):
    
    form = LoginForms()

    if request.method == 'POST':

        form = LoginForms(request.POST)

        if form.is_valid():

            nome = form['nome_login'].value()
            senha = form['senha'].value()

            autenticacao = Autenticacao(nome, senha)

            sessao = autenticacao.login(request)

            if not sessao:
                messages.error(request, 'Dados inválidos!')
                return redirect('login')
            
            elif sessao is None:
                messages.error(request, 'Usuario não cadastrado!')
                return redirect('login')
            
            else:
                return redirect('home')
            
    return render(request, 'app_usuarios/login.html', {'form': form})


def logout(request):

    autentic = Autenticacao()

    if autentic.logout(request):
        messages.success(request, 'Voce saiu da conta!')
        return redirect('index')
    else:
        messages.error(request, 'Erro ao sair')
        return redirect('index')


def cadastro(request):
    form = CadastroForms()

    if request.method == 'POST':

        form = CadastroForms(request.POST)

        if form.is_valid():
            
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'Senhas não são iguais!')
                return redirect('cadastro')
            
            nome = form['nome_cadastro'].value()
            senha = form['senha_1'].value()
            peso = form['peso'].value()
            altura = form['altura'].value()

            if Usuario.objects.filter(nome_usuario=nome).exists():
                messages.error(request, 'Usuário já cadastrado!')
                return redirect('cadastro')
            
            novo_usuario = Usuario(nome_usuario=nome, senha=senha, peso=peso, altura=altura)
            novo_usuario.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('login')

        else:
            messages.error(request, 'Dados cadastrais inválidos')
            return redirect('cadastro')

    return render(request, 'app_usuarios/cadastro.html', {'form': form})


def menu(request):

    #variavel de sessão
    id_usuario = request.session.get('id_usuario', None)

    #busca banco de dados
    obj_usuario = Usuario.objects.get(id=id_usuario)

    #gerando o formulário
    form = UsuarioForms(instance=obj_usuario)

    if request.method == 'POST':
        form = UsuarioForms(request.POST, instance=obj_usuario)

        if form.is_valid():
            form.save()

            return redirect('update_usuario')

    return render(request, 'app_usuarios/menu.html', {'form': form})


def registra_peso(request):
    
    #variavel de sessão
    id_usuario = request.session.get('id_usuario', None)

    #busca banco de dados
    obj_usuario = Usuario.objects.get(id=id_usuario)

    registro_pesos = PesoUsuario.objects.all()

    if request.method == 'POST':

        peso_form = request.POST.get('peso', None)

        novo_registro_peso = PesoUsuario(peso=peso_form, usuario=obj_usuario) #criando novo registro

        obj_usuario.peso = peso_form #atualizando na tabela usuarios
        obj_usuario.save()

        novo_registro_peso.save()
        
        messages.success(request, 'Peso atualizado')

    return render(request, 'app_usuarios/registra_peso.html', {'registro_pesos': registro_pesos})


def senha(request):
    
    #variavel de sessão
    id_usuario = request.session.get('id_usuario', None)

    #busca banco de dados
    obj_usuario = Usuario.objects.get(id=id_usuario)

    if request.method == 'POST':

        senha_form = request.POST.get('senha', None)

        if senha_form == obj_usuario.senha:

            nova_senha = request.POST.get('newsenha', None)

            obj_usuario.senha = nova_senha

            obj_usuario.save()

            messages.success(request, 'Senha alterada com sucesso!')

            return redirect('home')
        
        else:
            messages.error(request, 'Senha incorreta!')
            return redirect('senha')
    
    return render(request, 'app_usuarios/senha.html')


def gera_senha(request):

    #variavel de sessão
    id_usuario = request.session.get('id_usuario', None)

    senha_temp = gerador_de_senha()

    if request.method == 'POST':

        username = request.POST.get('username', None)

        obj_usuario = Usuario.objects.get(nome_usuario=username)

        obj_usuario.senha = senha_temp

        obj_usuario.save()

        return render(request, 'app_usuarios/gera_senha.html', {'senha_temp': senha_temp, 'delay': 5000, 'local': 'login'})
    
    if id_usuario is not None:

        #busca banco de dados
        obj_usuario = Usuario.objects.get(id=id_usuario)

        obj_usuario.senha = senha_temp

        obj_usuario.save()

        return render(request, 'app_usuarios/gera_senha.html', {'senha_temp': senha_temp, 'delay': 5000, 'local': 'senha'})
    
    return render(request, 'app_usuarios/gera_senha.html')


def gerador_de_senha():
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMENOPQRSTUVWXYZ1234567890!@#$%&*'
    senha = ''

    for c in range(0, 6):
        senha += caracteres[random.randint(0, len(caracteres))]

    return senha