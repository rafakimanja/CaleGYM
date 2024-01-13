from django.contrib import admin
from app.models import DiasTreino


class ListagemRegistro(admin.ModelAdmin):
    list_display = ('id', 'treino', 'registro', 'usuario')


admin.site.register(DiasTreino, ListagemRegistro)

