from django.db import models

class Comentario(models.Model):
    comentario = models.TextField()