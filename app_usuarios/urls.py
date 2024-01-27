from django.urls import path
from app_usuarios import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logout/', views.logout, name='logout'),
    path('update-usuario/', views.update_usuario, name='update_usuario'),
    path('registra_peso/', views.registra_peso, name='registra_peso')
]