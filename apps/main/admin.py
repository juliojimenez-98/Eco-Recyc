from django.contrib import admin
from apps.main.models import usuario, misiones, registro, puntosLimpios, premios, usuarioPremio

# Register your models here.
admin.site.register(usuario)
admin.site.register(misiones)
admin.site.register(registro)
admin.site.register(puntosLimpios)
admin.site.register(premios)
admin.site.register(usuarioPremio)