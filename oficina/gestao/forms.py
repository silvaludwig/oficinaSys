from django import forms
from .models import Cliente, Veiculo, Orcamento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.validators import validate_email
from django.core.exceptions import ValidationError

class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label="Email",
        help_text="Informe um email válido",
        validators=[validate_email]
    )
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Este email já está cadastrado.")
        return email
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Melhorias nos labels e help texts
        self.fields['username'].label = "Nome de usuário"
        self.fields['username'].help_text = "Obrigatório. 150 caracteres ou menos. Letras, números e @/./+/-/_ apenas."
        self.fields['password1'].help_text = """
            <ul>
                <li>Sua senha não pode ser muito parecida com suas outras informações pessoais.</li>
                <li>Sua senha deve conter pelo menos 8 caracteres.</li>
                <li>Sua senha não pode ser uma senha comumente usada.</li>
                <li>Sua senha não pode ser inteiramente numérica.</li>
            </ul>
        """

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        # fields = '__all__'
        exclude = ['usuario']  # 👈 exclua o campo usuario
        widgets = {
            'data_nascimento': forms.DateInput(attrs={'type': 'date'}),
        }
    
    def clean_cpf(self):
        cpf = self.cleaned_data['cpf']
        if not cpf.isdigit() or len(cpf) != 11:
            raise ValidationError('CPF deve conter exatamente 11 dígitos numéricos.')
        return cpf

class VeiculoForm(forms.ModelForm):
    class Meta:
        model = Veiculo
        # fields = '__all__'
        exclude = ['usuario']  # 👈 exclua o campo usuario
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
        }

class OrcamentoForm(forms.ModelForm):
    class Meta:
        model = Orcamento
        # fields = '__all__'
        exclude = ['usuario', 'data_cadastro']
        widgets = {
            'cliente': forms.Select(attrs={'class': 'form-select'}),
            'veiculo': forms.Select(attrs={'class': 'form-select'}),
            'data_validade': forms.DateInput(attrs={'type': 'date'}),
            'observacoes': forms.Textarea(attrs={'rows': 3}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'cliente' in self.data:
            try:
                cliente_id = int(self.data.get('cliente'))
                self.fields['veiculo'].queryset = Veiculo.objects.filter(cliente_id=cliente_id)
            except (ValueError, TypeError):
                pass
        elif self.instance.pk:
            self.fields['veiculo'].queryset = self.instance.cliente.veiculos.all()