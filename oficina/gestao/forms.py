from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class CadastroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.is_superuser = True  # Garante que seja superusuário
        if commit:
            user.save()
        return user
    

class VeiculoForm(forms.ModelForm):
    ...

class OrcamentoForm(forms.ModelForm):
    ...

class ClienteForm(forms.ModelForm):
    ...

