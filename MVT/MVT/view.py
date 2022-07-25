from django.http import HttpResponse, httprResponse
from django.shortcuts import render

def familia (resquest):
    return render(resquest,"template.html", context={""})
