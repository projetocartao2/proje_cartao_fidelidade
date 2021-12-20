
from django.urls import path, include
from .views import *

urlpatterns = [
    path('listar/', listar_usuarios, name='listar_usuarios'),
    path('cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
    #path('listar/<int:id>', listar_usuario_id, name='listar_usuario_id'),
    #path('editar/<int:id>', editar_usuario, name='editar_usuario'),
    #path('remover/<int:id>', remover_usuario, name='remover_usuario'),
]