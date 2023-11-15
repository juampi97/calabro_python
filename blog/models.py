from django.db import models

from datetime import date

categoria_options = [
    ('deportes','DEPORTES'),
    ('politica','POLITICA'),
    ('economia','ECONOMIA'),
    ('tecnologia','TECNOLOGIA'),
]
# Create your models here.
class Articulo(models.Model):
    titulo = models.CharField(max_length=40) 
    subtitulo = models.CharField(max_length=40) 
    categoria = models.CharField(max_length=40, choices=categoria_options, null=False, blank=False) 
    autor = models.CharField(max_length=40, null=False, default='')
    fecha = models.DateField(default=date.today())
    cuerpo = models.CharField(max_length=255)