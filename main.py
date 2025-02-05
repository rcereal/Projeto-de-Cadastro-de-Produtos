# import flet as ft
# from aplicativo.rotas.rotas import navegar_para

# def main(page: ft.Page):
#     navegar_para(page, "login")

# if __name__ == "__main__":
#     ft.app(target=main)

import flet as ft
from aplicativo.navegacao.navegacao import navegar_para

def main(page: ft.Page):
    page.title = 'Gestão de Produtos'
    page.window.width = 400
    page.padding = 20

    # Iniciar a aplicação na tela de login
    navegar_para(page, "login")

if __name__ == "__main__":
    ft.app(target=main)