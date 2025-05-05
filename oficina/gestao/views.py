from django.shortcuts import render
from .models import Veiculo, Orcamento, Cliente
from .forms import VeiculoForm, ClienteForm, CadastroUsuarioForm, OrcamentoForm
from django.contrib.auth import login
from django.shortcuts import render, redirect, get_object_or_404


def index(request):
    return render(request, "gestao/index.html")


def lista_veiculos(request):
    return render(request, "gestao/lista_veiculos.html")


def lista_clientes(request): 
    return render(request, "gestao/lista_clientes.html")


def lista_orcamentos(request): 
    return render(request, "gestao/lista_orcamentos.html")


def novo_veiculo(request): 
    return render(request, "gestao/novo_veiculo.html")


def novo_cliente(request): 
    return render(request, "gestao/novo_cliente.html")


def novo_orcamento(request): 
    return render(request, "gestao/novo_orcamento.html")


def editar_veiculo(request): 
    return render(request, "gestao/form_veiculo.html")


def editar_cliente(request): 
    return render(request, "gestao/form_cliente.html")


def editar_orcamento(request): 
    return render(request, "gestao/form_orcamento.html")


def excluir_veiculo(request): 
    return render(request, "gestao/confirmar_delete.html")


def excluir_cliente(request): 
    return render(request, "gestao/confirmar_delete.html")


def excluir_orcamento(request):
    return render(request, "gestao/confirmar_delete.html")

def cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Loga o usuário automaticamente após o cadastro
            return redirect(
                "index"
            )  # Substitua pelo nome da sua URL de redirecionamento
    else:
        form = CadastroUsuarioForm()
    return render(request, "gestao/cadastro_usuario.html", {"form": form})