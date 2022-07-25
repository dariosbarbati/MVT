from django.contrib import admin
from django.urls import path
from MVT.view import familia
from personas.views import create_person


urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', familia, name= "familia"),
    path('crear_persona/', create_person, name= "crear_persona")
]
