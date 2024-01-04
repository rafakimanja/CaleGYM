from django.contrib import admin
from app.models import Pessoa


class ListagemPessoas(admin.ModelAdmin):
    list_display = ('id', 'nome')
    list_display_links = ('id', 'nome')


admin.site.register(Pessoa, ListagemPessoas)

