from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.contrib import messages
from .models import Sala, Reserva
from .forms import ReservaForm

def lista_salas(request):
    salas = Sala.objects.all()
    return render(request, 'reservas/lista_salas.html', {'salas': salas})

def detalle_sala(request, pk):
    sala = get_object_or_404(Sala, pk=pk)
    reserva_activa = Reserva.objects.filter(sala=sala, hora_fin__gt=timezone.now()).first()
    return render(request, 'reservas/detalle_sala.html', {'sala': sala, 'reserva': reserva_activa})

def crear_reserva(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                form.save()  # ejecuta save() del modelo Reserva
                messages.success(request, 'Reserva creada correctamente.')
                return redirect('lista_salas')
            except ValueError as e:
                form.add_error(None, str(e))
    else:
        form = ReservaForm()
    return render(request, 'reservas/crear_reserva.html', {'form': form})
