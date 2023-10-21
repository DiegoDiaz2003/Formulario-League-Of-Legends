from django.urls import path
from . import views

urlpatterns = [
    path('participante/', views.formulario, name='formulario'),
]
