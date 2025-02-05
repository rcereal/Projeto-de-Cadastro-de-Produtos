import requests

def cadastrar_produto(produto, preco, categoria):
    if not produto.strip() or not preco.strip() or not categoria:
        return "Preencha todos os campos"
    
    try:
        preco = float(preco)
        if preco <= 0:
            return "O preço deve ser maior que zero"
    except ValueError:
        return "O preço deve ser um número valido"

    return f'aqui sera colocado o link para enviar os dados do backend'