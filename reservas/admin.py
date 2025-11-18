from django.contrib import admin
from .models import Sala, Reserva

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'habilitada', 'esta_reservada')
    list_filter = ('habilitada',)

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('sala', 'rut', 'hora_inicio', 'hora_fin')
    list_filter = ('sala',)
    readonly_fields = ('hora_inicio',)
    fields = ('sala', 'rut', 'hora_inicio', 'hora_fin')
