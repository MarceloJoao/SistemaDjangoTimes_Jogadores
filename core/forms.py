from django import forms
from .models import Time, Jogador
#usando ModelForm para customiar os forms
class TimeForm(forms.ModelForm):
    class Meta:
        model = Time
        fields = ['nome', 'cidade']

#formulario de jogador
class JogadorForm(forms.ModelForm):
    class Meta:
        model = Jogador
        fields = ['nome', 'posicao', 'idade', 'time']
