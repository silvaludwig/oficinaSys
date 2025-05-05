from django.contrib.auth import views as auth_views
from django.urls import path
from . import views
from .views import cadastro_usuario


urlpatterns = [
    path("", views.index, name="index"),
    path("veiculos/", views.lista_veiculos, name="lista_veiculos"),
    path("veiculos/novo/", views.novo_veiculo, name="novo_veiculo"),
    path("veiculos/editar/<int:id>/", views.editar_veiculo, name="editar_veiculo"),
    path("veiculos/excluir/<int:id>/", views.excluir_veiculo, name="excluir_veiculo"),
    path("clientes/", views.lista_clientes, name="lista_clientes"),
    path("clientes/novo/", views.novo_cliente, name="novo_cliente"),
    path("clientes/editar/<int:id>/", views.editar_cliente, name="editar_cliente"),
    path("clientes/excluir/<int:id>/", views.excluir_cliente, name="excluir_cliente"),
    path("orcamentos/", views.lista_orcamentos, name="lista_orcamentos"),
    path("orcamentos/novo/", views.novo_orcamento, name="novo_orcamento"),
    path("orcamentos/editar/<int:id>/", views.editar_orcamento, name="editar_orcamento"),
    path("orcamentos/excluir/<int:id>/", views.excluir_orcamento, name="excluir_orcamento"),
    path("accounts/login/", auth_views.LoginView.as_view(), name="login"),
    path("accounts/logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("cadastro/", cadastro_usuario, name="cadastro_usuario"),
]
