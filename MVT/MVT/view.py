from django.http import HttpResponse
from django.shortcuts import render

def bienvenido (resquest):
    return render(resquest,'bienvenido.html', context={})
