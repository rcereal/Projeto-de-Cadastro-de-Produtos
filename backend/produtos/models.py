from django.db import models
from decimal import Decimal


class Categoria(models.Model):
    nome = models.CharField(
        max_length=100, 
        unique=True, 
        verbose_name="Nome da Categoria", 
        help_text="Digite o nome da categoria. Deve ser único."
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ['nome']


class Produto(models.Model):
    nome = models.CharField(
        max_length=100, 
        verbose_name="Nome do Produto", 
        help_text="Digite o nome do produto."
    )
    preco = models.TextField()
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        verbose_name="Categoria do Produto", 
        help_text="Selecione a categoria deste produto."
    )

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Produto"
        verbose_name_plural = "Produtos"
        ordering = ['nome']
