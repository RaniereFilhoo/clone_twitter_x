from django.db import models

class Home(models.Model):
    nome = models.CharField(max_length=30)
    comentario = models.TextField()
