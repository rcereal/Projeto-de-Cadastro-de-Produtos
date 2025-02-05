from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate
from .models import *
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import HttpResponseNotAllowed

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

@csrf_exempt
def produto_cadastrar(request):
    if request.method == 'POST':
        entradafe = json.loads(request.body)
        nome = entradafe.get('nome', '').strip()
        preco = entradafe.get('preco')
        if isinstance(preco, str):
            preco = preco.strip()
        categoria_id = entradafe.get('categoria_id', '').strip()

        if not nome or not preco or not categoria_id:
            return JsonResponse({'error': 'Mensagem detalhada do erro'}, status=400)
        
        try:
            preco = float(preco)
            if preco <= 0:
                return JsonResponse({'error': "O preço deve ser maior que zero"}, status=400)
            # preco = str(preco)
        except ValueError:
            return JsonResponse({'error': 'O preço deve ser um número válido'}, status=400)

        try:
            categoria = Categoria.objects.get(id=categoria_id)
        except Categoria.DoesNotExist:
            return JsonResponse({'error': 'Categoria não encontrada'}, status=400)
        
        produto = Produto.objects.create(nome=nome, preco=preco, categoria=categoria)

        return JsonResponse({
            'id': produto.id,
            'nome': produto.nome,
            'preco': str(produto.preco),
            'categoria': produto.categoria.nome
        }, status=201)
    
    return HttpResponseNotAllowed(['POST'], 'Método não permitido.')

@csrf_exempt
def listar_produto(request):
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