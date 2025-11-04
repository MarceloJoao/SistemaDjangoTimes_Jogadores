from django.urls import path
from . import views

urlpatterns = [
    # Times
    path('times/', views.lista_times, name='lista_times'),
    path('novo/', views.novo_time, name='novo_time'),
    path('editar/<int:id>/', views.editar_time, name='editar_time'),
    path('deletar/<int:id>/', views.deletar_time, name='deletar_time'),

    # Jogadores
    path('jogadores/', views.lista_jogadores, name='lista_jogadores'),
    path('jogadores/novo/', views.novo_jogador, name='novo_jogador'),
    path('jogadores/editar/<int:id>/', views.editar_jogador, name='editar_jogador'),
    path('jogadores/deletar/<int:id>/', views.deletar_jogador, name='deletar_jogador'),
]
