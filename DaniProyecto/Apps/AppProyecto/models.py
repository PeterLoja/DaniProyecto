from django.db import models


# Create your models here.

class Cuestionario(models.Model):
    nombre = models.CharField(max_length=200, null=True, blank=True)
    pregunta1 = models.CharField(max_length=200, null=True, blank=True)
    pregunta2 = models.CharField(max_length=200, null=True, blank=True)
    pregunta3 = models.CharField(max_length=200, null=True, blank=True)
    pregunta4 = models.CharField(max_length=200, null=True, blank=True)
    pregunta5 = models.CharField(max_length=200, null=True, blank=True)
    pregunta6 = models.CharField(max_length=200, null=True, blank=True)
    pregunta7 = models.CharField(max_length=200, null=True, blank=True)
    pregunta8 = models.CharField(max_length=200, null=True, blank=True)