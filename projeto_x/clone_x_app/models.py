from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth import get_user_model
import math

def get_default_user():
    User = get_user_model()
    user, created = User.objects.get_or_create(username='admin')
    return user.id

class Comentario(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default=get_default_user)
    comentario = models.TextField()
    imagem = models.ImageField(upload_to='imagens_comentarios/', null=True, blank=True)
    data_criacao = models.DateTimeField(default=timezone.now)
    
    def tempo_desde_criacao(self):
        agora = timezone.now()
        diferenca = agora - self.data_criacao
        if diferenca.days == 0 and diferenca.seconds < 60:
            segundos = diferenca.seconds
            if segundos == 0:
                return "Agora"
            else:
                return f"{segundos} s"
        elif diferenca.days == 0 and diferenca.seconds < 3600:
            minutos = math.floor(diferenca.seconds / 60)
            if minutos == 1:
                return "1 min"
            else:
                return f"{minutos} min"
        elif diferenca.days == 0 and diferenca.seconds < 86400:
            horas = math.floor(diferenca.seconds / 3600)
            if horas == 1:
                return "1 h"
            else:
                return f"{horas} h"

class Perfil(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    foto = models.ImageField(upload_to='fotos_usuarios/', null=True, blank=True)
    
    def foto_url(self):
        if self.foto:
            return self.foto.url
        else:
            return None