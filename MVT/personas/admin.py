from django.contrib import admin
from personas.models import Persona

# Register your models here.
# admin.site.register(Persona)

@admin.register(Persona)
class Persona_admin(admin.ModelAdmin):
    list_display = ["name", "last_name", "parent", "ages"]
