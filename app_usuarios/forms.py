from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label='Nome de Login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'input-control',
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
                'class': 'input-control',
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
                'class': 'input-control',
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
                'class': 'input-control',
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
                'class': 'input-control',
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
                'class': 'input-control',
                'placeholder': 'Kg'
            }
        )
    )
    altura = forms.IntegerField(
        label='Digite a sua altura',
        required=True,
        widget=forms.NumberInput(
            attrs={
                'class': 'input-control',
                'placeholder': 'Cm'
            }
        )
    )