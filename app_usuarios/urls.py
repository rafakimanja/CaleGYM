from django.urls import path
from app_usuarios import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('gera_senha/', views.gera_senha, name='gera_senha'),
    path('logout/', views.logout, name='logout'),
    path('menu/', views.menu, name='menu'),
    path('registra_peso/', views.registra_peso, name='registra_peso'),
    path('senha/', views.senha, name='senha')
]