from django.urls import path
from . import views

urlpatterns = [
    path('api/categorias/', views.categoria_list, name='categoria_list'),
    path('api/cadastrar_produto/', views.produto_cadastrar, name='produto_cadastrar'),
    path('api/login_usuario/', views.login_usuario, name='login_usuario'),
    path('api/listar_produtos/', views.listar_produtos, name='listar_produtos'),
    path('api/gerenciar_produto/', views.gerenciar_produto, name='gerenciar_produto'),
    path('api/excluir_produto/<int:produto_id>/', views.excluir_produto, name='excluir_produto'),
]