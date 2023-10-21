from django.db import models

class Participante(models.Model):
    nombre_invocador = models.CharField(max_length=100)
    nivel = models.IntegerField()
    rol_principal = models.CharField(max_length=50)
    campeon_principal = models.CharField(max_length=50)
    rango = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre_invocador

