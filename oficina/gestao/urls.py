from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import (
    cadastro_usuario,
    BuscaClienteView,
    OrcamentoDetailView,
    custom_logout,
)

urlpatterns = [
    # Páginas principais
    path("", views.index, name="index"),
    path("dashboard/", views.dashboard, name="dashboard"),
    
    # Rotas para Veículos
    path("veiculos/", views.lista_veiculos, name="lista_veiculos"),
    path("veiculos/novo/", views.novo_veiculo, name="novo_veiculo"),
    path("veiculos/editar/<int:id>/", views.editar_veiculo, name="editar_veiculo"),
    path("veiculos/excluir/<int:id>/", views.excluir_veiculo, name="excluir_veiculo"),
    path("veiculos/<int:id>/", views.detalhe_veiculo, name="detalhe_veiculo"),
    
    # Rotas para Clientes
    path("clientes/", BuscaClienteView.as_view(), name="lista_clientes"),
    path("clientes/novo/", views.novo_cliente, name="novo_cliente"),
    path("clientes/editar/<int:id>/", views.editar_cliente, name="editar_cliente"),
    path("clientes/excluir/<int:id>/", views.excluir_cliente, name="excluir_cliente"),
    path("clientes/<int:id>/", views.detalhe_cliente, name="detalhe_cliente"),
    
    # Rotas para Orçamentos
    path("orcamentos/", views.lista_orcamentos, name="lista_orcamentos"),
    path("orcamentos/novo/", views.novo_orcamento, name="novo_orcamento"),
    path("orcamentos/editar/<int:id>/", views.editar_orcamento, name="editar_orcamento"),
    path("orcamentos/excluir/<int:id>/", views.excluir_orcamento, name="excluir_orcamento"),
    path("orcamentos/<int:pk>/", OrcamentoDetailView.as_view(), name="detalhe_orcamento"),
    path("orcamentos/relatorio/", views.relatorio_orcamentos, name="relatorio_orcamentos"),
    
    # Autenticação
    path("accounts/login/", auth_views.LoginView.as_view(
        template_name='gestao/auth/login.html',
        extra_context={'title': 'Login'}
    ), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(
        template_name='gestao/auth/logout.html',
        extra_context={'title': 'Logout'}, 
        next_page='index'
    ), name="logout"),
    # path('accounts/logout/', custom_logout, name='logout'),
    path("accounts/password_reset/", auth_views.PasswordResetView.as_view(
        template_name='gestao/auth/password_reset.html',
        email_template_name='gestao/auth/password_reset_email.html',
        subject_template_name='gestao/auth/password_reset_subject.txt'
    ), name="password_reset"),
    path("accounts/password_reset/done/", auth_views.PasswordResetDoneView.as_view(
        template_name='gestao/auth/password_reset_done.html'
    ), name="password_reset_done"),
    path("accounts/reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(
        template_name='gestao/auth/password_reset_confirm.html'
    ), name="password_reset_confirm"),
    path("accounts/reset/done/", auth_views.PasswordResetCompleteView.as_view(
        template_name='gestao/auth/password_reset_complete.html'
    ), name="password_reset_complete"),
    path("accounts/password_change/", auth_views.PasswordChangeView.as_view(
        template_name='gestao/auth/password_change.html'
    ), name="password_change"),
    path("accounts/password_change/done/", auth_views.PasswordChangeDoneView.as_view(
        template_name='gestao/auth/password_change_done.html'
    ), name="password_change_done"),
    
    # Cadastro de usuário
    path("cadastro/", cadastro_usuario, name="cadastro_usuario"),
    
    # API (opcional)
    path("api/clientes/", views.api_clientes, name="api_clientes"),
    path("api/veiculos/", views.api_veiculos, name="api_veiculos"),
]