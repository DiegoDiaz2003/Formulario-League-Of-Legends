from django.shortcuts import render, redirect, get_object_or_404
from .forms import ParticipanteForm
from .models import Participante

def formulario(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            participante = form.save()
            return redirect('participante_detalle', pk=participante.pk)
    else:
        form = ParticipanteForm()

    return render(request, 'index.html', {'form': form})
