from tabnanny import verbose
from django.db import models

# Creo la clase Persona la cual va a ser cada familiar

class Persona(models.Model):
    name = models.CharField(max_length=40)
    last_name= models.CharField(max_length=40)
    parent=models.CharField(max_length=40)
    ages= models.IntegerField()
    date = models.DateField(auto_now_add=True)

def __str__(self):
    return self.name

# Para que en la admin de django corriga el plural
# class Meta:
#     verbose_name = "Producto"
#     verbose_name_plural = "Productos"
