from django import forms
from .models import Participante

class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre_invocador', 'nivel', 'rol_principal', 'campeon_principal', 'rango']
