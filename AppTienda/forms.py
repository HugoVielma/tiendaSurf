from django import forms
from . models import Cliente, Producto

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion','email']
class Productos(forms.ModelForm):
     class Meta:
         model= Producto
         fields = ['nombre', 'descripcion', 'precio']