from multiprocessing import context
import re
from django.shortcuts import render
from personas.models import Persona

#Creo la funcion para agregar personas a la odb

def create_person(resquest):
    new_person=Persona.objects.create(name="Patricia", last_name="Sbarbati", parent="Tia", ages=58)
    context={
        "new_person":new_person
    }
    return render(resquest, "new_person.html", context=context)
