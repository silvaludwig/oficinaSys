from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login
from .models import Veiculo, Orcamento, Cliente
from .forms import VeiculoForm, ClienteForm, CadastroUsuarioForm, OrcamentoForm
from django.db.models import Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView


# Views Públicas
def index(request):
    return render(request, "gestao/index.html")

def cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Cadastro realizado com sucesso!")
            return redirect("index")
    else:
        form = CadastroUsuarioForm()
    return render(request, "gestao/cadastro_usuario.html", {"form": form})

# Views Protegidas (requerem login)
@login_required
def lista_veiculos(request):
    veiculos = Veiculo.objects.all().order_by('-id')
    return render(request, "gestao/veiculo/lista.html", {'veiculos': veiculos})

@login_required
def lista_clientes(request): 
    clientes = Cliente.objects.all().order_by('-id')
    return render(request, "gestao/cliente/lista.html", {'clientes': clientes})

@login_required
def lista_orcamentos(request): 
    orcamentos = Orcamento.objects.all().order_by('-data_cadastro')
    return render(request, "gestao/orcamento/lista.html", {'orcamentos': orcamentos})

@login_required
def novo_veiculo(request):
    if request.method == "POST":
        form = VeiculoForm(request.POST)
        if form.is_valid():
            veiculo = form.save()
            messages.success(request, "Veículo cadastrado com sucesso!")
            return redirect('lista_veiculos')
    else:
        form = VeiculoForm()
    return render(request, "gestao/veiculo/formulario.html", {'form': form, 'titulo': 'Novo Veículo'})

@login_required
def novo_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            cliente = form.save()
            messages.success(request, "Cliente cadastrado com sucesso!")
            return redirect('lista_clientes')
    else:
        form = ClienteForm()
    return render(request, "gestao/cliente/formulario.html", {'form': form, 'titulo': 'Novo Cliente'})

@login_required
def novo_orcamento(request):
    if request.method == "POST":
        form = OrcamentoForm(request.POST)
        if form.is_valid():
            orcamento = form.save(commit=False)
            orcamento.responsavel = request.user
            orcamento.save()
            messages.success(request, "Orçamento criado com sucesso!")
            return redirect('lista_orcamentos')
        else:
            print("\n=== Erros do formulário ===")  # Debug
            print(form.errors)  # Mostra todos os erros de validação
    else:
        form = OrcamentoForm()
    
    return render(request, "gestao/orcamento/formulario.html", {
        'form': form,
        'titulo': 'Novo Orçamento'
    })


@login_required
def editar_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == "POST":
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            messages.success(request, "Veículo atualizado com sucesso!")
            return redirect('lista_veiculos')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, "gestao/veiculo/formulario.html", {'form': form, 'titulo': 'Editar Veículo'})

@login_required
def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, "Cliente atualizado com sucesso!")
            return redirect('lista_clientes')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, "gestao/cliente/formulario.html", {'form': form, 'titulo': 'Editar Cliente'})

@login_required
def editar_orcamento(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    if request.method == "POST":
        form = OrcamentoForm(request.POST, instance=orcamento)
        if form.is_valid():
            form.save()
            orcamento.responsavel = request.user
            orcamento.save()
            messages.success(request, "Orçamento atualizado com sucesso!")
            return redirect('lista_orcamentos')
    else:
        form = OrcamentoForm(instance=orcamento)
    return render(request, "gestao/orcamento/formulario.html", {'form': form, 'titulo': 'Editar Orçamento'})

@login_required
def excluir_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    if request.method == "POST":
        veiculo.delete()
        messages.success(request, "Veículo excluído com sucesso!")
        return redirect('lista_veiculos')
    return render(request, "gestao/veiculo/confirmar_delete.html", {'objeto': veiculo, 'tipo': 'veículo'})

@login_required
def excluir_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == "POST":
        cliente.delete()
        messages.success(request, "Cliente excluído com sucesso!")
        return redirect('lista_clientes')
    return render(request, "gestao/cliente/confirmar_delete.html", {'objeto': cliente, 'tipo': 'cliente'})

@login_required
def excluir_orcamento(request, id):
    orcamento = get_object_or_404(Orcamento, id=id)
    if request.method == "POST":
        orcamento.delete()
        messages.success(request, "Orçamento excluído com sucesso!")
        return redirect('lista_orcamentos')
    return render(request, "gestao/orcamento/confirmar_delete.html", {'objeto': orcamento, 'tipo': 'orçamento'})


# View para busca de clientes
class BuscaClienteView(LoginRequiredMixin, ListView):
    model = Cliente
    template_name = 'gestao/cliente/lista.html'
    context_object_name = 'clientes'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            return Cliente.objects.filter(
                Q(nome__icontains=query) |
                Q(cpf__icontains=query) |
                Q(email__icontains=query))
        return Cliente.objects.all().order_by('-data_cadastro')

# View detalhada para orçamento
class OrcamentoDetailView(LoginRequiredMixin, DetailView):
    model = Orcamento
    template_name = 'gestao/orcamento/detalhe.html'
    context_object_name = 'orcamento'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Detalhes do Orçamento'
        return context
    

@login_required
def dashboard(request):
    total_clientes = Cliente.objects.count()
    total_veiculos = Veiculo.objects.count()
    total_orcamentos = Orcamento.objects.count()
    orcamentos_pendentes = Orcamento.objects.filter(status='pendente').count()
    
    context = {
        'total_clientes': total_clientes,
        'total_veiculos': total_veiculos,
        'total_orcamentos': total_orcamentos,
        'orcamentos_pendentes': orcamentos_pendentes,
    }
    return render(request, 'gestao/dashboard.html', context)

@login_required
def detalhe_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    veiculos = cliente.veiculos.all()
    orcamentos = cliente.orcamentos.all()
    
    return render(request, 'gestao/cliente/detalhe.html', {
        'cliente': cliente,
        'veiculos': veiculos,
        'orcamentos': orcamentos,
    })

@login_required
def detalhe_veiculo(request, id):
    veiculo = get_object_or_404(Veiculo, id=id)
    orcamentos = veiculo.orcamentos.all()
    
    return render(request, 'gestao/veiculo/detalhe.html', {
        'veiculo': veiculo,
        'orcamentos': orcamentos,
    })

@login_required
def relatorio_orcamentos(request):
    orcamentos = Orcamento.objects.all()
    total = sum(o.valor for o in orcamentos if o.foi_pago)
    
    return render(request, 'gestao/orcamento/relatorio.html', {
        'orcamentos': orcamentos,
        'total': total,
    })


# API Views
@login_required
def api_veiculos(request):
    cliente_id = request.GET.get('cliente_id')
    if cliente_id:
        veiculos = Veiculo.objects.filter(cliente_id=cliente_id).values('id', 'marca', 'modelo', 'placa')
        return JsonResponse(list(veiculos), safe=False)
    return JsonResponse([], safe=False)

@login_required
def api_clientes(request):
    termo = request.GET.get('q')
    if termo:
        clientes = Cliente.objects.filter(
            Q(nome__icontains=termo) | Q(cpf__icontains=termo))
        results = [{'id': c.id, 'text': f'{c.nome} (CPF: {c.cpf})'} for c in clientes]
        return JsonResponse({'results': results})
    return JsonResponse({'results': []})

# Dashboard View
@login_required
def dashboard(request):
    total_clientes = Cliente.objects.count()
    total_veiculos = Veiculo.objects.count()
    total_orcamentos = Orcamento.objects.count()
    orcamentos_pendentes = Orcamento.objects.filter(status='pendente').count()
    ultimos_orcamentos = Orcamento.objects.all().order_by('-data_cadastro')[:5]
    ultimos_clientes = Cliente.objects.all().order_by('-data_cadastro')[:5]
    
    context = {
        'total_clientes': total_clientes,
        'total_veiculos': total_veiculos,
        'total_orcamentos': total_orcamentos,
        'orcamentos_pendentes': orcamentos_pendentes,
        'ultimos_orcamentos': ultimos_orcamentos,
        'ultimos_clientes': ultimos_clientes,
    }
    return render(request, 'gestao/dashboard.html', context)
