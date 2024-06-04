from django.db import models
import math
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.conf import settings

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
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to='fotos_perfil/', blank=True, null=True)

    def __str__(self):
        return self.user.username

