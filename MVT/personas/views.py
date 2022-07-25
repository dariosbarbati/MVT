from multiprocessing import context
import re
from django.shortcuts import render
from personas.models import Persona

#Creo la funcion para agregar personas a la odb

def create_person(resquest):
    new_person=Persona.objects.create(name="Leandro", last_name="Sbarbati", parent="Hermano", ages=42)
    context={
        "new_person":new_person,
    }
    return render(resquest, "new_person.html", context=context)

def list_person(resquest):
    persons=Persona.objects.all()
    context={"persons": persons}
    return  render(resquest,"list.html",context=context) 
