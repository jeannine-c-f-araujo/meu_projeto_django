from django import forms
from helloworld.models import Funcionario

class InsereFuncionarioForm(forms.ModelForm):
    chefe = forms.BooleanField(
        label='Este Funcionário exerce função de Chefia?',
        required=True,
    )
    biografia = forms.CharField(
        label='Biografia',
        required=False,
        widget=forms.Textarea
    )

    class Meta:
        model = Funcionario

        fields = [
            'nome',
            'sobrenome',
            'cpf',
            'remuneracao'
        ]

        exclude = [
            'tempo_de_servico'
        ]
