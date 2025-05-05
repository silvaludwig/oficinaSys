from django.db import models


class Cliente(models.Model):
    nome = models.CharField(max_length=50, null=False)
    email = models.CharField(max_length=50, null=False)
    cpf = models.IntegerField(unique=True, null=False)
    endereco = models.CharField(max_length=150, null=False)
    telefoe = models.IntegerField(null=False)
    data_nascimento = models.DateField()
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    ano_fabricacao = models.IntegerField(null=False)
    motor = models.CharField(max_length=50)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    data_cadastro = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Marca: {self.marca}, Modelo: {self.modelo}, Ano de Fabricação: {self.ano_fabricacao}"


class Orcamento(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=8, decimal_places=2)
    foi_pago = models.BooleanField(default=True)
    data_cadastro = models.DateTimeField(auto_now_add=True)
    forma_pagamento = models.CharField(
        max_length=20,
        choices=[
            ("dinheiro", "Dinheiro"),
            ("pix", "PIX"),
            ("transferencia", "Transferência"),
            ("boleto", "Boleto"),
            ("outro", "Outro"),
        ],
        default="pix",
    )

    def __str__(self):
        return f"Nome do Cliente: {self.cliente.nome} | Veículo: {self.veiculo.marca}, {self.veiculo.modelo} | Valor do orçamento: R${self.valor}"
