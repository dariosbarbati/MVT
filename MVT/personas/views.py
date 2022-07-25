from multiprocessing import context
import re
from django.shortcuts import render
from personas.models import Persona

# Creo la funcion para agregar personas a la odb
# Antes de ir a http://127.0.0.1:8000/crear_persona/ modificar los siguientes parametros y reiniciar servidor

def create_person(resquest):
    new_person=Persona.objects.create(name="--", last_name="--", parent="--", ages=0)
    context={
        "new_person":new_person,
    }
    return render(resquest, "new_person.html", context=context)

def list_person(resquest):
    persons=Persona.objects.all()
    context={"persons": persons}
    return  render(resquest,"list.html",context=context) 
