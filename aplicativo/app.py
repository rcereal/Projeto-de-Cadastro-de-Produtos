# app.py
# import flet as ft
# import requests

# def tela_cadastro_produtos(page):
#     page.title = 'Cadastro de Produtos'
#     page.window_width = 400

#     titulo_produto = ft.Text('Nome do produto')
#     produto = ft.TextField(label='Digite o nome do produto')
#     titulo_preco = ft.Text('Preço do produto')
#     preco = ft.TextField(label='Digite o preço do produto')
#     titulo_categoria = ft.Text('Categoria')

#     categorias = requests.get('http://localhost:8000/api/categorias/')
#     categorias_json = categorias.json()
#     categoria = ft.Dropdown(
#         label='Selecione a categoria do produto',
#         options=[ft.dropdown.Option(key=str(categ['id']), text=categ['nome']) for categ in categorias_json]
#     )

#     def on_cadastrar(e):
#         produto_nome = produto.value
#         produto_preco = preco.value
#         categoria_id = categoria.value

#         if not produto_nome.strip():
#             snackbar = ft.SnackBar(content=ft.Text('O campo "Nome do produto" é obrigatório.'))
#             page.add(snackbar)
#             snackbar.open = True
#             return

#         if not produto_preco.strip():
#             snackbar = ft.SnackBar(content=ft.Text('O campo "Preço do produto" é obrigatório.'))
#             page.add(snackbar)
#             snackbar.open = True
#             return

#         if not categoria_id:
#             snackbar = ft.SnackBar(content=ft.Text('Por favor selecione uma categoria.'))
#             page.add(snackbar)
#             snackbar.open = True
#             return

#         try:
#             produto_preco = float(produto_preco.replace(',', '.'))
#         except ValueError:
#             snackbar = ft.SnackBar(content=ft.Text('O preço deve ser um número válido.'))
#             page.add(snackbar)
#             snackbar.open = True
#             return

#         try:
#             response = requests.post(
#                 'http://localhost:8000/api/cadastrar_produto/',
#                 json={
#                     'nome': produto_nome,
#                     'preco': produto_preco,
#                     'categoria_id': categoria_id
#                 }
#             )

#             if response.status_code == 201:
#                 produto_cadastrado = response.json()
#                 snackbar = ft.SnackBar(content=ft.Text(f'Produto {produto_cadastrado["nome"]} cadastrado com sucesso.'))
#                 page.add(snackbar)
#                 snackbar.open = True
#             else:
#                 error_cadastro = response.json().get("error", "Erro desconhecido")
#                 snackbar = ft.SnackBar(content=ft.Text(f'Erro ao cadastrar produto: {error_cadastro}'))
#                 page.add(snackbar)
#                 snackbar.open = True
#         except Exception as ex:
#             snackbar = ft.SnackBar(content=ft.Text(f"Erro ao se conectar ao servidor: {str(ex)}"))
#             page.add(snackbar)
#             snackbar.open = True

    # def on_ver_lista(e):
    #     try:
    #         response = requests.get('http://localhost:8000/api/listar_produtos/')
    #         produtos = response.json()
    #         lista_produtos = ft.Column(
    #             [
    #                 ft.Text(f'Produto: {produto["nome"]}, Preço: {produto["preco"]}, Categoria: {produto["categoria"]}')
    #                 for produto in produtos
    #             ]
    #         )
    #         page.add(lista_produtos)
            
    #     except requests.exceptions.JSONDecodeError as e:
    #         snackbar = ft.SnackBar(content=ft.Text(f"Erro ao decodificar JSON: {e}"))
    #         page.add(snackbar)
    #         snackbar.open = True
    #     except Exception as e:
    #         snackbar = ft.SnackBar(content=ft.Text(f"Erro ao carregar lista de produtos: {e}"))
    #         page.add(snackbar)
    #         snackbar.open = True

    # botao_cadastrar = ft.ElevatedButton(
    #     text='Cadastrar',
    #     on_click=on_cadastrar
    # )
    
    # botao_ver_lista = ft.ElevatedButton(
    #     text='Ver a Lista de Produtos',
    #     on_click=on_ver_lista
    # )

    # page.add(
    #     titulo_produto,
    #     produto,
    #     titulo_preco,
    #     preco,
    #     titulo_categoria,
    #     categoria,
    #     botao_cadastrar,
    #     botao_ver_lista,
    # )

# -------------------------------------------------------------

# import flet as ft
# import requests

# def tela_cadastro_produtos(page):
#     page.title = 'Cadastro de Produtos'
#     page.window_width = 400
#     page.padding = 20

#     titulo_produto = ft.Text('Nome do produto', weight="bold", size=14)
#     produto = ft.TextField(label='Digite o nome do produto', width=300)

#     titulo_preco = ft.Text('Preço do produto', weight="bold", size=14)
#     preco = ft.TextField(label='Digite o preço do produto', width=300)

#     titulo_categoria = ft.Text('Categoria', weight="bold", size=14)

#     try:
#         categorias = requests.get('http://localhost:8000/api/categorias/')
#         categorias_json = categorias.json()
#         categoria_options = [
#             ft.dropdown.Option(key=str(categ['id']), text=categ['nome']) for categ in categorias_json
#         ]
#     except Exception:
#         categoria_options = []

#     categoria = ft.Dropdown(
#         label='Selecione a categoria do produto',
#         options=categoria_options,
#         width=300
#     )

#     def show_snackbar(message, color="red"):
#         """Exibe um snackbar com mensagem."""
#         snackbar = ft.SnackBar(content=ft.Text(message), bgcolor=color)
#         page.snack_bar = snackbar
#         snackbar.open = True
#         page.update()

#     def on_cadastrar(e):
#         """Função para cadastrar produto."""
#         produto_nome = produto.value.strip()
#         produto_preco = preco.value.strip()
#         categoria_id = categoria.value

#         if not produto_nome:
#             show_snackbar('O campo "Nome do produto" é obrigatório.')
#             return

#         if not produto_preco:
#             show_snackbar('O campo "Preço do produto" é obrigatório.')
#             return

#         if not categoria_id:
#             show_snackbar('Por favor selecione uma categoria.')
#             return

#         try:
#             produto_preco = float(produto_preco.replace(',', '.'))
#         except ValueError:
#             show_snackbar('O preço deve ser um número válido.')
#             return

#         try:
#             response = requests.post(
#                 'http://localhost:8000/api/cadastrar_produto/',
#                 json={'nome': produto_nome, 'preco': produto_preco, 'categoria_id': categoria_id}
#             )

#             if response.status_code == 201:
#                 produto_cadastrado = response.json()
#                 show_snackbar(f'Produto {produto_cadastrado["nome"]} cadastrado com sucesso.', color="green")
#                 page.bottom_sheet.open = False
#                 page.update()
#             else:
#                 error_cadastro = response.json().get("error", "Erro desconhecido")
#                 show_snackbar(f'Erro ao cadastrar produto: {error_cadastro}')
#         except Exception as ex:
#             show_snackbar(f"Erro ao se conectar ao servidor: {str(ex)}")

#     botao_cadastrar = ft.ElevatedButton(text='Cadastrar', on_click=on_cadastrar, width=140)

#     return ft.Container(
#         content=ft.Column([
#             titulo_produto, produto,
#             titulo_preco, preco,
#             titulo_categoria, categoria,
#             ft.Row([botao_cadastrar], alignment="center")
#         ], spacing=10),
#         padding=15,
#         border_radius=10,
#         bgcolor="#F5F5F5",
#         alignment=ft.alignment.center
#     )

# ----------------------------------------------------------------------------------

import flet as ft
import requests
import threading

def tela_principal(page):
    page.clean()
    page.title = "Cadastro de Produtos"
    page.window_width = 400

    titulo = ft.Text("Cadastro de Produtos", text_align="center")

    botao_cadastrar = ft.ElevatedButton(
        text="Cadastrar Produto",
        on_click=lambda e: tela_cadastro_produtos(page)
    )

    botao_ver_produtos = ft.ElevatedButton(
        text="Ver Produtos",
        on_click=lambda e: tela_ver_produtos(page)
    )

    page.add(
        titulo,
        botao_cadastrar,
        botao_ver_produtos
    )

def tela_cadastro_produtos(page):
    page.clean()
    titulo_produto = ft.Text("Nome do Produto:")
    produto = ft.TextField(label="Digite o nome do produto")

    titulo_preco = ft.Text("Preço:")
    preco = ft.TextField(label="Digite o preço")

    titulo_categoria = ft.Text("Categoria:")
    categoria = ft.TextField(label="Digite a categoria")

    def on_cadastrar(e):
        try:
            response = requests.post(
                "http://localhost:8000/api/cadastrar_produto/",
                json={"nome": produto.value, "preco": preco.value, "categoria": categoria.value}
            )

            if response.status_code == 201:
                snackbar = ft.SnackBar(content=ft.Text("Produto cadastrado com sucesso!"), open=True)
            else:
                error = response.json().get("error", "Erro desconhecido")
                snackbar = ft.SnackBar(content=ft.Text(f"Erro ao cadastrar: {error}"), open=True)

            page.snack_bar = snackbar
            page.update()
        except Exception as ex:
            snackbar = ft.SnackBar(content=ft.Text(f"Erro ao conectar ao servidor: {ex}"), open=True)
            page.snack_bar = snackbar
            page.update()

    botao_cadastrar = ft.ElevatedButton(text="Cadastrar", on_click=on_cadastrar)

    botao_voltar = ft.ElevatedButton(text='Voltar', on_click=lambda e: tela_principal(page))

    page.clean()
    page.add(
        titulo_produto,
        produto,
        titulo_preco,
        preco,
        titulo_categoria,
        categoria,
        botao_cadastrar,
        botao_voltar
    )

def tela_ver_produtos(page):
    page.clean()

    lista_produtos = ft.Column()
    status_text = ft.Text("Carregando...")  # Mensagem de carregamento

    def carregar_produtos():
        try:
            response = requests.get("http://localhost:8000/api/listar_produtos/")
            produtos = response.json()

            page.controls.remove(status_text)

            titulo = ft.Text("Lista de Produtos", text_align="center")
            lista_produtos.controls = [titulo] 
            
            lista_produtos.controls = [
                ft.Text(f'Produto: {produto["nome"]}, Preço: {produto["preco"]}, Categoria: {produto["categoria"]}')
                for produto in produtos
            ]
            status_text.value = ""  # Remove o texto "Carregando..."
        except requests.exceptions.JSONDecodeError as e:
            status_text.value = f"Erro ao decodificar JSON: {e}"
        except Exception as e:
            status_text.value = f"Erro ao carregar lista de produtos: {e}"
        
        page.update()

    # Executa a requisição em uma thread para não travar a interface
    threading.Thread(target=carregar_produtos, daemon=True).start()

    botao_atualizar = ft.ElevatedButton(text="Atualizar Lista", on_click=lambda e: threading.Thread(target=carregar_produtos, daemon=True).start())
    botao_voltar = ft.ElevatedButton(text="Voltar", on_click=lambda e: tela_principal(page))

    page.add(status_text, lista_produtos, botao_atualizar, botao_voltar)