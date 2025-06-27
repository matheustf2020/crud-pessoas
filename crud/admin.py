from django.contrib import admin
from .models import Pessoa, Cargos, Projetos

admin.site.register(Pessoa)
admin.site.register(Cargos)
admin.site.register(Projetos)
