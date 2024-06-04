from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['comentario', 'imagem']
        widgets = {
            'comentario': forms.Textarea(attrs={'placeholder': 'O que está acontecendo?'}),
        }
    def __init__(self, *args, **kwargs):
        super(ComentarioForm, self).__init__(*args, **kwargs)
        self.fields['imagem'].widget.attrs.update({'id': 'id_imagem'})
