from django.db import models

# Creo la clase Persona la cual va a ser cada familiar

class   Persona(models.Model):
    name = models.CharField(max_length=40)
    last_name= models.CharField(max_length=40)
    age= models.IntegerField()
    date = models.DateField(auto_now_add=True)

