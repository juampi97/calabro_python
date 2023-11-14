from django.db import models

from datetime import date

# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=40) 
    subtitulo = models.CharField(max_length=40) 
    categoria = models.CharField(max_length=40) 
    # autor = models.CharField(max_length=40)
    fecha = models.DateField(default=date.today())
    cuerpo = models.CharField(max_length=255)