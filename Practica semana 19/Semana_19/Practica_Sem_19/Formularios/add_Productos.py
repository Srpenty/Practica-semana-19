from django import forms

class addProducto(forms.Form):
    nombre = forms.CharField(max_length=100)
    stock = forms.IntegerField()