from django.urls import path
from . import views

urlpatterns = [
    path('api/categorias/', views.categoria_list, name='categoria_list'),
    path('api/cadastrar_produto/', views.produto_cadastrar, name='produto_cadastrar'),
    path('api/login_usuario/', views.login_usuario, name='login_usuario'),
    path('api/listar_produtos/', views.listar_produto, name='lista_produtos'),
    path('api/gerenciar_produto/', views.gerenciar_produto, name='gerenciar_produto')
]