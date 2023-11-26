from Practica_Sem_19.models import Proveedores
from django import forms

class addProveedor(forms.Form):
    nombre = forms.CharField(max_length=100)
    telefono = forms.CharField(max_length=12)