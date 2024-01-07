from django.contrib import admin
from app.models import Pessoa, DiasTreino


class ListagemPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')


class ListagemRegistro(admin.ModelAdmin):
    list_display = ('id', 'treino', 'registro')

admin.site.register(Pessoa, ListagemPessoas)
admin.site.register(DiasTreino, ListagemRegistro)

