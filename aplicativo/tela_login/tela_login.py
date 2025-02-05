# import flet as ft
# import requests
# from aplicativo.app import tela_cadastro_produtos

# def tela_login(page):
#     page.title = "Login de Usuario"
#     page.window.width = 400

#     titulo_email = ft.Text('Email:')
#     email = ft.TextField(label='Digite seu email...')
#     titulo_senha = ft.Text('Senha:')
#     senha = ft.TextField(label='Digite sua senha...', password=True)

#     def autenticar_usuario(e):
#         email_usuario = email.value.strip()
#         senha_usuario = senha.value.strip()

#         if not email_usuario or not senha_usuario:
#             snackbar = ft.SnackBar(content='Por favor, preencha todos os campos.', open=True)
#             page.add(snackbar)
#             return

#         try:
#             response = requests.post(
#                 'http://127.0.0.1:8000/api/login_usuario/',
#                 json={'email': email_usuario, 'senha': senha_usuario}
#             )
#             if response.status_code == 200:
#                 page.clean()
#                 tela_cadastro_produtos(page)
#             else:
#                 error = response.json().get('error', 'Erro desconhecido')
#                 snackbar = ft.SnackBar(content=ft.Text(f'Erro: {error}'), open=True)
#                 page.add(snackbar)
#         except Exception as ex:
#             print(f'Erro ao autenticar usuario: {ex}')
#             snackbar = ft.SnackBar(content=ft.Text(f'Erro ao se conectar ao servidor: {str(ex)}'), open=True)
#             page.add(snackbar)

#     botao_login = ft.ElevatedButton(text='Entrar', on_click=autenticar_usuario)

#     page.add(
#         titulo_email,
#         email,
#         titulo_senha,
#         senha,
#         botao_login
#     )

import flet as ft
import requests
from aplicativo.app import tela_principal

def tela_login(page):
    page.title = "Login de Usuário"
    page.window.width = 400

    titulo_email = ft.Text('Email:')
    email = ft.TextField(label='Digite seu email...')
    titulo_senha = ft.Text('Senha:')
    senha = ft.TextField(label='Digite sua senha...', password=True)

    def autenticar_usuario(e):
        email_usuario = email.value.strip()
        senha_usuario = senha.value.strip()

        if not email_usuario or not senha_usuario:
            snackbar = ft.SnackBar(content=ft.Text('Por favor, preencha todos os campos.'), open=True)
            page.snack_bar = snackbar
            page.update()
            return

        try:
            response = requests.post(
                'http://127.0.0.1:8000/api/login_usuario/',
                json={'email': email_usuario, 'senha': senha_usuario}
            )

            if response.status_code == 200:
                page.clean()
                tela_principal(page)
            else:
                error = response.json().get('error', 'Erro desconhecido')
                snackbar = ft.SnackBar(content=ft.Text(f'Erro: {error}'), open=True)
                page.snack_bar = snackbar
                page.update()
        except Exception as ex:
            print(f'Erro ao autenticar usuário: {ex}')
            snackbar = ft.SnackBar(content=ft.Text(f'Erro ao se conectar ao servidor: {str(ex)}'), open=True)
            page.snack_bar = snackbar
            page.update()

    botao_login = ft.ElevatedButton(text='Entrar', on_click=autenticar_usuario)

    page.add(
        titulo_email,
        email,
        titulo_senha,
        senha,
        botao_login
    )
