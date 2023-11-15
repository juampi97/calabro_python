from django import forms

from blog.models import Articulo
class ArticuloPostForm(forms.ModelForm):
    class Meta:
        model = Articulo
        fields = ['titulo', 'subtitulo', 'categoria', 'cuerpo']

        widgets = {
            'titulo': forms.TextInput(attrs={'class':'form-control'}),
            'subtitulo': forms.TextInput(attrs={'class':'form-control'}),
            'categoria': forms.Select(attrs={'class':'form-control'}),
            'cuerpo': forms.Textarea(attrs={'class':'form-control'})
        }
