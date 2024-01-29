from django import forms
from app_usuarios.models import Usuario

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Seu nome de Login'
            }
        )
    )
    senha = forms.CharField(
        label='Senha',
        required=True,
        max_length=25,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Sua senha'
            }
        )
    )


class CadastroForms(forms.Form):
    nome_cadastro = forms.CharField(
        label='Nome de Cadastro',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Seu nome de Cadastro'
            }
        )
    )
    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=25,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Até 25 caracteres'
            }
        )
    )
    senha_2 = forms.CharField(
        label='Sua senha novamente',
        required=True,
        max_length=25,
        widget=forms.PasswordInput(
            attrs={
                'placeholder': 'Digite sua senha novamente'
            }
        )
    )
    peso = forms.DecimalField(
        label='Digite o seu peso',
        required=True,
        max_digits=5,
        decimal_places=2,
        widget=forms.NumberInput(
            attrs = {
                'placeholder': 'em Kg'
            }
        )
    )
    altura = forms.IntegerField(
        label='Digite a sua altura',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'em Cm'
            }
        )
    )

class UsuarioForms(forms.ModelForm):
    class Meta:
        model = Usuario
        exclude = ['senha',]
        labels = {
            'nome_usuario': 'Nome de Usuário',
            'peso': 'Peso (em KG)',
            'altura': 'Altura (em Cm)',
            'imc': 'IMC'
        }
        widgets = {
            'nome_usuario': forms.TextInput(),
            'peso': forms.NumberInput(),
            'altura': forms.NumberInput(),
            'imc': forms.NumberInput()
        }