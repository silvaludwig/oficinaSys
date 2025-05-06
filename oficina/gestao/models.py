from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError
import re

def validate_cpf(value):
    if not re.match(r'^\d{11}$', str(value)):
        raise ValidationError('CPF deve conter exatamente 11 dígitos.')

def validate_phone(value):
    if not re.match(r'^\d{10,11}$', str(value)):
        raise ValidationError('Telefone deve conter 10 ou 11 dígitos.')

class Cliente(models.Model):
    nome = models.CharField(max_length=100, null=False, verbose_name="Nome Completo")
    email = models.EmailField(max_length=100, null=False, unique=True)
    cpf = models.CharField(
        max_length=11, 
        unique=True, 
        null=False,
        validators=[validate_cpf],
        verbose_name="CPF (apenas números)"
    )
    endereco = models.CharField(max_length=150, null=False, verbose_name="Endereço")
    telefone = models.CharField(
        max_length=11, 
        null=False,
        validators=[validate_phone],
        verbose_name="Telefone (apenas números)"
    )
    data_nascimento = models.DateField(verbose_name="Data de Nascimento")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"{self.nome} (CPF: {self.cpf})"


class Veiculo(models.Model):
    MARCA_CHOICES = [
        ('chevrolet', 'Chevrolet'),
        ('fiat', 'Fiat'),
        ('volkswagen', 'Volkswagen'),
        ('ford', 'Ford'),
        ('toyota', 'Toyota'),
        ('hyundai', 'Hyundai'),
        # Adicione outras marcas conforme necessário
    ]
    
    marca = models.CharField(
        max_length=50,
        choices=MARCA_CHOICES,
        verbose_name="Marca do Veículo"
    )
    modelo = models.CharField(max_length=50, verbose_name="Modelo")
    ano_fabricacao = models.IntegerField(
        null=False,
        validators=[
            MinValueValidator(1900),
            MaxValueValidator(2025)
        ],
        verbose_name="Ano de Fabricação"
    )
    placa = models.CharField(
        max_length=7,
        unique=True,
        null=True,
        blank=True,
        verbose_name="Placa (sem hífen)"
    )
    motor = models.CharField(max_length=50, verbose_name="Motor")
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        related_name='veiculos',
        verbose_name="Proprietário"
    )
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Cadastro")

    class Meta:
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"{self.get_marca_display()} {self.modelo} ({self.ano_fabricacao}) - {self.placa}"


class Orcamento(models.Model):
    STATUS_CHOICES = [
        ('pendente', 'Pendente'),
        ('aprovado', 'Aprovado'),
        ('recusado', 'Recusado'),
        ('finalizado', 'Finalizado'),
    ]
    
    FORMA_PAGAMENTO_CHOICES = [
        ("dinheiro", "Dinheiro"),
        ("pix", "PIX"),
        ("transferencia", "Transferência"),
        ("cartao_credito", "Cartão de Crédito"),
        ("cartao_debito", "Cartão de Débito"),
        ("boleto", "Boleto"),
        ("outro", "Outro"),
    ]
    
    cliente = models.ForeignKey(
        Cliente, 
        on_delete=models.CASCADE,
        related_name='orcamentos',
        verbose_name="Cliente"
    )
    veiculo = models.ForeignKey(
        Veiculo, 
        on_delete=models.CASCADE,
        related_name='orcamentos',
        verbose_name="Veículo"
    )
    valor = models.DecimalField(
        max_digits=10, 
        decimal_places=2,
        verbose_name="Valor Total"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='pendente',
        verbose_name="Status do Orçamento"
    )
    foi_pago = models.BooleanField(default=False, verbose_name="Foi Pago?")
    data_cadastro = models.DateTimeField(auto_now_add=True, verbose_name="Data de Criação")
    data_validade = models.DateField(verbose_name="Data de Validade")
    forma_pagamento = models.CharField(
        max_length=20,
        choices=FORMA_PAGAMENTO_CHOICES,
        default="pix",
        verbose_name="Forma de Pagamento"
    )
    observacoes = models.TextField(
        blank=True,
        null=True,
        verbose_name="Observações"
    )
    responsavel = models.ForeignKey(
        'auth.User',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name="Responsável"
    )

    class Meta:
        verbose_name = "Orçamento"
        verbose_name_plural = "Orçamentos"
        ordering = ['-data_cadastro']

    def __str__(self):
        return f"Orçamento #{self.id} - {self.cliente.nome} - R$ {self.valor}"