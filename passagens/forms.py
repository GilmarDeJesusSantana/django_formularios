from django import forms
from django.forms import Textarea
from tempus_dominus.widgets import DatePicker
from datetime import date
from passagens.classes_viagem import tipos_de_classe


class PassagensForms(forms.Form):
    origem = forms.CharField(label='Origem', max_length=100)
    destino = forms.CharField(label='Destino', max_length=100)
    data_ida = forms.DateField(label='Ida', widget=DatePicker())
    data_volta = forms.DateField(label='Volta', widget=DatePicker())
    data_pesquisa = forms.DateField(label='Data da pesquisa', disabled=True, initial=date.today())
    classe_viagem = forms.ChoiceField(label='Classe do vôo', choices=tipos_de_classe)
    informacoes = forms.CharField(
        label='Informações extras ',
        max_length=200,
        widget=Textarea(),
        required=False
    )
    email = forms.EmailField(label='E-mail',max_length=200)
