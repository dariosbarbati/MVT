from django.contrib import admin
from django.urls import path
from MVT.view import bienvenido
from personas.views import create_person,list_person


urlpatterns = [
    path('admin/', admin.site.urls),
    path('bienvenido/', bienvenido, name= "bienvenida"),
    path('crear_persona/', create_person, name= "crear_persona"),
    path('lista/', list_person, name= "listar_personas") 
]
