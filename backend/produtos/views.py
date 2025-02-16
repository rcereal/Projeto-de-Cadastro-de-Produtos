from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseNotAllowed
from decimal import Decimal

@csrf_exempt
def login_usuario(request):
    if request.method == 'POST':
        dados = json.loads(request.body)
        email = dados.get('email', '')
        senha = dados.get('senha', '')
        if not email or not senha:
            return JsonResponse({'error': 'Email e senha são obrigatorios.'}, status=400)
        
        user = authenticate(username=email, password=senha)
        if user is not None:
            return JsonResponse({'message': 'Login realizado com sucesso.'}, status=200)
        else:
            return JsonResponse({'error': 'Email ou senha invalidos.'}, status=401)
        
    return JsonResponse({'error': 'Método não permitido.'}, status=405)

@csrf_exempt
def categoria_list(request):
    if request.method == 'GET':
        categorias = Categoria.objects.all()
        categorias_entradafe = [{'id': categ.id, 'nome': categ.nome} for categ in categorias]
        return JsonResponse(categorias_entradafe, safe=False)

    elif request.method == 'POST':
        entradafe = json.loads(request.body)
        nome = entradafe.get('nome', '').strip()

        if not nome:
            return JsonResponse({'error': 'Nome é obrigatório'}, status=400)

        nova_categoria = Categoria.objects.create(nome=nome)
        return JsonResponse({'id': nova_categoria.id, 'nome': nova_categoria.nome})

# @csrf_exempt
# def produto_cadastrar(request):
#     if request.method == 'POST':
#         entradafe = json.loads(request.body)
#         nome = entradafe.get('nome', '').strip()
#         preco = entradafe.get('preco')
#         if isinstance(preco, str):
#             preco = preco.strip()
#         categoria_id = entradafe.get('categoria_id', '')

#         if not nome or not preco or not categoria_id:
#             return JsonResponse({'error': 'Mensagem detalhada do erro'}, status=400)
        
#         try:
#             preco = float(preco)
#             if preco <= 0:
#                 return JsonResponse({'error': "O preço deve ser maior que zero"}, status=400)
#             preco = str(preco)
#         except ValueError:
#             return JsonResponse({'error': 'O preço deve ser um número válido'}, status=400)

#         try:
#             categoria = Categoria.objects.get(id=categoria_id)
#         except Categoria.DoesNotExist:
#             return JsonResponse({'error': 'Categoria não encontrada'}, status=400)
        
#         produto = Produto.objects.create(nome=nome, preco=preco, categoria=categoria)

#         return JsonResponse({
#             'id': produto.id,
#             'nome': produto.nome,
#             'preco': str(produto.preco),
#             'categoria': produto.categoria.nome
#         }, status=201)
    
#     return HttpResponseNotAllowed(['POST'], 'Método não permitido.')

# @csrf_exempt
# def gerenciar_produto(request, produto_id):
#     try:
#         produto = Produto.objects.get(id=produto_id)

#     except Produto.DoesNotExist:
#         return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    
#     if request.method == 'PUT':
#         try:
#             entradafe = json.loads(request.body)
#             nome = entradafe.get('nome', '').strip()
#             preco = entradafe.get('preco')
#             categoria_id = entradafe.get('categoria_id').strip()

#             if not nome or not preco or not categoria_id:
#                 return JsonResponse({'error': 'Todos os campos são obrigatórios'}, status=400)
            
#             try:
#                 preco = float(preco)
#                 if preco <= 0:
#                     return JsonResponse({'error': 'O preço deve ser maior que zero'}, status=400)
#             except ValueError:
#                 return JsonResponse({'error': 'O preço deve ser um número valido'}, status=400)
            
#             try:
#                 categoria  = Categoria.objects.get(id=categoria_id)
#             except Categoria.DoesNotExist:
#                 return JsonResponse({'error': 'Categoria não encontrada'}, status=404)
            
#             produto.nome = nome
#             produto.preco = preco
#             produto.categoria = categoria
#             produto.save()

#             return JsonResponse({
#                 'id': produto.id,
#                 'nome': produto.nome,
#                 'preco': str(produto.preco),
#                 'categoria': produto.categoria.nome
#             }, status=200)
    
#         except json.JSONDecodeError:
#             return JsonResponse({'error': 'Erro ao processar JSON'}, status=400)
        
#     return HttpResponseNotAllowed(['PUT'])

def validar_preco(preco_str):
    # Substitui a vírgula por ponto
    preco_str = preco_str.replace(',', '.')
    
    # Verifica se o valor tem apenas números e ponto
    if not all(c.isdigit() or c == '.' for c in preco_str):
        raise ValueError('O preço deve conter apenas números e ponto ou vírgula.')

    # Converte para Decimal e arredonda para 2 casas decimais
    preco = Decimal(preco_str)
    return preco

@csrf_exempt
def produto_cadastrar(request):
    if request.method == 'POST':
        entradafe = json.loads(request.body)
        nome = entradafe.get('nome', '').strip()
        preco = entradafe.get('preco')
        categoria_id = entradafe.get('categoria_id', '')

        if not preco:
            return JsonResponse({'error': 'O preço é obrigatório.'}, status=400)
        
        try:
            preco = validar_preco(preco)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=400)

        if not nome or not categoria_id:
            return JsonResponse({'error': 'Todos os campos são obrigatórios'}, status=400)

        try:
            categoria = Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoria não encontrada'}, status=404)

        # Salvar o produto
        produto = Produto.objects.create(nome=nome, preco=str(preco), categoria=categoria)

        return JsonResponse({
            'id': produto.id,
            'nome': produto.nome,
            'preco': str(produto.preco),  # Exibe o preço como string
            'categoria': produto.categoria.nome
        }, status=201)

    return HttpResponseNotAllowed(['POST'])

@csrf_exempt
def gerenciar_produto(request, produto_id):
    try:
        produto = Produto.objects.get(id=produto_id)
    except Produto.DoesNotExist:
        return JsonResponse({'error': 'Produto não encontrado'}, status=404)

    if request.method == 'PUT':
        try:
            entradafe = json.loads(request.body)
            nome = entradafe.get('nome', '').strip()
            preco = entradafe.get('preco')
            categoria_id = entradafe.get('categoria_id').strip()

            if not nome or not preco or not categoria_id:
                return JsonResponse({'error': 'Todos os campos são obrigatórios'}, status=400)

            preco = validar_preco(preco)

            try:
                categoria = Categoria.objects.get(id=categoria_id)
            except Categoria.DoesNotExist:
                return JsonResponse({'error': 'Categoria não encontrada'}, status=404)

            produto.nome = nome
            produto.preco = str(preco)  # Armazenar como string
            produto.categoria = categoria
            produto.save()

            return JsonResponse({
                'id': produto.id,
                'nome': produto.nome,
                'preco': str(produto.preco),  # Exibe o preço como string
                'categoria': produto.categoria.nome
            }, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Erro ao processar JSON'}, status=400)

    return HttpResponseNotAllowed(['PUT'])

@csrf_exempt
def listar_produtos(request):
    produtos = Produto.objects.all()
    produtos_json = []
    for produto in produtos:
        produtos_json.append({
            'id': produto.id,
            'nome': produto.nome,
            'preco': str(produto.preco),
            'categoria': produto.categoria.nome
        })
    return JsonResponse(produtos_json, safe=False)

@csrf_exempt
def excluir_produto(request, produto_id):
    if request.method == 'DELETE':
        try:
            produto = Produto.objects.get(id=produto_id)
            produto.delete()
            return JsonResponse({'message': 'Produto deletado com sucesso'}, status=200)
        except Produto.DoesNotExist:
            return JsonResponse({'error': 'Produto não encontrado'}, status=404)
    else:
        return JsonResponse({'error': 'Método não permitido'}, status=405)