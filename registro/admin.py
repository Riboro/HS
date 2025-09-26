from django.contrib import admin
from registro.models import Registro


class Registros(admin.ModelAdmin):

        list_display = ('id', 'nome', 'numero')
        list_display_links = ('id', 'numero')
        

        


admin.site.register(Registro, Registros)
