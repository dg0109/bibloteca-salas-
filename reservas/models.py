from django.db import models
from django.utils import timezone
from datetime import timedelta

class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField()
    habilitada = models.BooleanField(default=True)

    def __str__(self):
        return self.nombre

    @property
    def esta_reservada(self):
        ahora = timezone.now()
        return self.reserva_set.filter(hora_fin__gt=ahora).exists()

class Reserva(models.Model):
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE)
    rut = models.CharField(max_length=12)
    hora_inicio = models.DateTimeField(editable=False)
    hora_fin = models.DateTimeField()


    def save(self, *args, **kwargs):
        ahora = timezone.now()
        if not self.pk:
            self.hora_inicio = ahora
            self.hora_fin = ahora + timedelta(hours=2)
            if Reserva.objects.filter(sala=self.sala, hora_fin__gt=self.hora_inicio).exists():
                raise ValueError("La sala ya está reservada en este momento.")
        super().save(*args, **kwargs)
