from django import forms
from .models import Comentario
from .models import Perfil

class PerfilForm(forms.ModelForm):
    class Meta:
        model = Perfil
        fields = ['foto']

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario', 'imagem']
        widgets = {
            'comentario': forms.Textarea(attrs={'placeholder': 'O que está acontecendo?'}),
        }