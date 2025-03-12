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
    page.window_width = 400
    page.window_height = 500
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    titulo = ft.Text(
        "Login",
        size=24,
        weight=ft.FontWeight.BOLD,
        text_align=ft.TextAlign.CENTER
    )

    email = ft.TextField(
        label="Digite seu email...",
        width=300,
        border_radius=8
    )
    senha = ft.TextField(
        label="Digite sua senha...",
        password=True,
        width=300,
        border_radius=8
    )

    def autenticar_usuario(e):
        email_usuario = email.value.strip()
        senha_usuario = senha.value.strip()

        if not email_usuario or not senha_usuario:
            page.snack_bar = ft.SnackBar(ft.Text("Por favor, preencha todos os campos."), open=True)
            page.update()
            return

        try:
            response = requests.post(
                "http://127.0.0.1:8000/api/login_usuario/",
                json={"email": email_usuario, "senha": senha_usuario}
            )

            if response.status_code == 200:
                page.clean()
                tela_principal(page)
            else:
                error = response.json().get("error", "Erro desconhecido")
                page.snack_bar = ft.SnackBar(ft.Text(f"Erro: {error}"), open=True)
                page.update()
        except Exception as ex:
            page.snack_bar = ft.SnackBar(ft.Text(f"Erro ao se conectar ao servidor: {str(ex)}"), open=True)
            page.update()

    botao_login = ft.ElevatedButton(
        text="Entrar",
        on_click=autenticar_usuario,
        width=300,
        bgcolor=ft.colors.BLUE,
        color=ft.colors.WHITE
    )

    container = ft.Container(
        content=ft.Column(
            [
                titulo,
                email,
                senha,
                botao_login
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        ),
        width=350,
        padding=20,
        border_radius=12,
        bgcolor=ft.colors.GREY_200
    )

    page.add(
        ft.Row([container], alignment=ft.MainAxisAlignment.CENTER)
    )