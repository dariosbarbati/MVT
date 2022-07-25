from django.http import HttpResponse
from django.shortcuts import render

def familia (resquest):
    return render(resquest,'template1.html', context={})
