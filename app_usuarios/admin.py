from django.contrib import admin
from app_usuarios.models import Usuario, PesoUsuario


class ListandoUsuarios(admin.ModelAdmin):

    def qtd_dias_treino(self, obj):
        return len(obj.diastreino_set.all())

    list_display = ('id', 'nome_usuario', 'qtd_dias_treino')
    list_display_links = ('id', 'nome_usuario')


admin.site.register(Usuario, ListandoUsuarios)


class ListandoPesoUsuarios(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'peso')
    list_display_links = ('id', 'usuario')


admin.site.register(PesoUsuario, ListandoPesoUsuarios)