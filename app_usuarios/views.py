from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CadastroForms, LoginForms
from .models import Usuario, PesoUsuario
from .authenticate import Autenticacao


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


def update_usuario(request):

    #variavel de sessão
    id_usuario = request.session.get('id_usuario', None)

    #busca banco de dados
    obj_usuario = Usuario.objects.get(id=id_usuario)

    #gerando o formulário
    form = CadastroForms(instance=obj_usuario)

    return render(request, 'app_usuarios/update_usuario.html', {'form': form})


def registra_peso(request):
    
    #variavel de sessão
    id_usuario = request.session.get('id_usuario', None)

    #busca banco de dados
    obj_usuario = Usuario.objects.get(id=id_usuario)

    if request.method == 'POST':

        peso_form = request.POST.get('peso', None)

        novo_registro_peso = PesoUsuario(peso=peso_form, usuario=obj_usuario) #criando novo registro

        obj_usuario.peso = peso_form #atualizando na tabela usuarios
        obj_usuario.save()

        novo_registro_peso.save()
        
        messages.success(request, 'Peso atualizado')
    
    calcula_IMC(request)

    return render(request, 'app_usuarios/registra_peso.html')


def calcula_IMC(request):

    #variavel de sessão
    id_usuario = request.session.get('id_usuario', None)    

    #busca banco de dados
    usuario = Usuario.objects.get(id=id_usuario)

    imc = usuario.peso / (usuario.altura ** 2)

    usuario.imc = imc

    usuario.save()