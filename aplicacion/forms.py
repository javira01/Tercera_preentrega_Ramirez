from django import forms

from aplicacion.models import Autor
from aplicacion.models import Genero

class LibroForm(forms.Form):
    titulo = forms.CharField(max_length=100, required=True, label='Título')
    autor = forms.ModelChoiceField(queryset=Autor.objects.all(), label='Autor')
    genero = forms.ModelChoiceField(queryset=Genero.objects.all(), label='Género')
    ano_publicacion = forms.IntegerField(min_value=0, label='Año de publicación')
    isbn = forms.CharField(max_length=13, label='ISBN')
