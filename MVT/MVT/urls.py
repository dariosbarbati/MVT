from django.contrib import admin
from django.urls import path
from MVT.view import familia



urlpatterns = [
    path('admin/', admin.site.urls),
    path('familia/', familia, name= "familia")
]
