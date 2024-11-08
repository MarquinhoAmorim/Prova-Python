from django import forms
from django.core.exceptions import ValidationError

class VagaForm(forms.Form):
    titulo = forms.CharField(max_length=150, required=True)
    empresa = forms.CharField(max_length=150, required=True)
    telefone = forms.CharField(max_length=20, required=True)
    descricao = forms.CharField(max_length=255, required=True, label='Descrição da Vaga')
    email = forms.EmailField(required=True, label='Email da Empresa')
    
    def clean_titulo(self):
        nome = self.cleaned_data['titulo']
        return nome.upper()

    def clean_empresa(self):
        empresa = self.cleaned_data['empresa']
        if len(empresa) < 2:
            raise ValidationError('Empresa precisa ter ao menos dois caracteres')
        return empresa.capitalize() 

    def clean_telefone(self):
        telefone = self.cleaned_data['telefone']
        if telefone.startswith('19'):
            return telefone
        raise ValidationError('DDD válido somente o 19')

    def clean_descricao(self):
        descricao = self.cleaned_data['descricao']
        if len(descricao) < 10:
            raise ValidationError('A descrição da vaga deve ter pelo menos 10 caracteres')
        return descricao

    def clean_email(self):
        email = self.cleaned_data['email']
        return email
