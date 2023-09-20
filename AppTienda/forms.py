from django import forms
from . models import Cliente, Cupon, Producto, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nombre', 'direccion','email']
class Productos(forms.ModelForm):
     class Meta:
         model= Producto
         fields = ['nombre', 'descripcion', 'precio']

class CompraCarrito(forms.ModelForm):
    class Meta:
        model = Compra
        fields = ['cliente', 'productos', 'cantidad']


class CuponForm(forms.ModelForm):
    class Meta:
        model = Cupon
        fields = ['codigo', 'descripcion']