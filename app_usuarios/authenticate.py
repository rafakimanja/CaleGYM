from django.core.exceptions import ObjectDoesNotExist
from app_usuarios.models import Usuario


class Autenticacao:

    def __init__(self, nome_usuario='', senha=''):
        self.nome_usuario = nome_usuario
        self.senha = senha

    def get_usuario(self):
        try:
            usuario = Usuario.objects.get(nome_usuario=self.nome_usuario)
            return usuario
        except ObjectDoesNotExist:
            return None

    def __verifica_login_usuario(self):

        usuario = self.get_usuario()

        if usuario is not None:

            if self.senha == usuario.senha and self.nome_usuario == usuario.nome_usuario:
                return True

            else:
                return False

        else:
            return None

    def login(self, request):

        usuario = self.get_usuario()

        if usuario is not None:

            if self.__verifica_login_usuario() is not None:

                if self.__verifica_login_usuario():
                    request.session['id_usuario'] = usuario.id
                    print(f'Sessão: {request.session["id_usuario"]}')
                    return True
                else:
                    return False

        return None

    def logout(self, request):

        if 'id_usuario' in request.session:
            del request.session['id_usuario']
            return True
        else:
            return False

    def verifica_sessao(self, request):
        id_usuario = request.session.get('id_usuario')
        if isinstance(id_usuario, int):
            return True
        else:
            return False
