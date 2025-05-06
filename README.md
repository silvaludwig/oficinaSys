# README - Sistema de Gestão para Oficina Mecânica

![Badge em Desenvolvimento](https://img.shields.io/badge/status-em%20desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Django](https://img.shields.io/badge/Django-4.0%2B-green)

## 📝 Descrição do Projeto

Sistema completo para gestão de oficinas mecânicas, desenvolvido em Django, que permite:
- Cadastro e gerenciamento de clientes
- Controle de veículos e seus proprietários
- Criação e acompanhamento de orçamentos
- Relatórios e dashboard administrativo

## ✨ Funcionalidades

- **Gestão de Clientes**
  - Cadastro completo com CPF, contatos e endereço
  - Histórico de veículos e orçamentos
  - Busca avançada

- **Controle de Veículos**
  - Registro detalhado (marca, modelo, ano, placa)
  - Vinculação automática ao cliente
  - Histórico de serviços

- **Orçamentos**
  - Criação com múltiplos itens
  - Status personalizáveis (pendente, aprovado, finalizado)
  - Controle de pagamentos
  - Relatórios financeiros

- **Dashboard**
  - Visão geral do negócio
  - Gráficos e métricas importantes
  - Acesso rápido às principais funcionalidades

## 🛠️ Tecnologias Utilizadas

- **Backend**
  - Python 3.8+
  - Django 4.0+
  - Django REST Framework (para APIs)

- **Frontend**
  - Bootstrap 5
  - Bootstrap Icons
  - HTML5 + CSS3
  - JavaScript básico

- **Banco de Dados**
  - SQLite (desenvolvimento)
  - PostgreSQL (produção recomendada)

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Python 3.8 ou superior
- Pip (gerenciador de pacotes)
- Virtualenv (recomendado)

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/oficina-mecanica.git
cd oficina-mecanica
```

2. Crie e ative um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate    # Windows
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Configure o banco de dados:
```bash
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Execute o servidor:
```bash
python manage.py runserver
```

7. Acesse no navegador:
```
http://localhost:8000
```

## 📦 Estrutura do Projeto

```
oficina-mecanica/
├── gestao/                 # App principal
│   ├── migrations/         # Migrações do banco
│   ├── templates/         # Templates HTML
│   ├── admin.py            # Config do Admin
│   ├── apps.py             # Config do App
│   ├── forms.py            # Formulários
│   ├── models.py           # Modelos de dados
│   ├── urls.py             # URLs do app
│   └── views.py            # Views
├── oficina/                # Projeto principal
│   ├── settings.py         # Configurações
│   ├── urls.py             # URLs globais
│   └── wsgi.py             # WSGI config
├── manage.py               # Script de gerenciamento
└── README.md               # Este arquivo
```

## 📚 Documentação Adicional

- [Documentação Django](https://docs.djangoproject.com/)
- [Bootstrap 5](https://getbootstrap.com/docs/5.0/getting-started/introduction/)
- [Guia de Estilo Python](https://www.python.org/dev/peps/pep-0008/)

## 🤝 Como Contribuir

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## 📄 Licença

Distribuído sob a licença MIT. Veja `LICENSE` para mais informações.

## ✉️ Contato

Ludwig S - silvaludwigg@gmail.com

Link do Projeto: [https://github.com/silvaludwig/oficinaSys](https://github.com/silvaludwig/oficinaSys)

---

**Nota:** Este projeto está em desenvolvimento ativo. Novas funcionalidades serão adicionadas regularmente.
