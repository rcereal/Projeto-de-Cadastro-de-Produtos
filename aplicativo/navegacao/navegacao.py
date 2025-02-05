import flet as ft
from aplicativo.app import tela_cadastro_produtos
from aplicativo.tela_login.tela_login import tela_login

def navegar_para(page, rota):
    page.clean()  # Limpa a tela antes de carregar a nova

    if rota == "login":
        tela_login(page)
    elif rota == "cadastro_produto":
        page.add(tela_cadastro_produtos(page))  # Adiciona a tela de cadastro corretamente

    page.update()
