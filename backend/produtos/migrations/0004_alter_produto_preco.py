# Generated by Django 5.1.4 on 2025-01-29 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0003_alter_produto_preco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco',
            field=models.CharField(help_text='Digite o preço do produto.', max_length=10, verbose_name='Preço do Produto'),
        ),
    ]
