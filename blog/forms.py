from django import forms

class ArticuloForm(forms.Form):
    titulo = forms.CharField(max_length=40) 
    subtitulo = forms.CharField(max_length=40) 
    categoria = forms.CharField(max_length=40) 
    autor = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=255)


class ComentarioForm(forms.Form):
    autor = forms.CharField(max_length=40)
    cuerpo = forms.CharField(max_length=255)