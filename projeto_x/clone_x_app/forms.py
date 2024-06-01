from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario', 'imagem']
        widgets = {
            'comentario': forms.Textarea(attrs={'placeholder': 'O que está acontecendo?'}),
        }