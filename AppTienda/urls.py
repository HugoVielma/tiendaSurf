from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name="inicio"),
    path('cliente/',cliente, name="cliente"),
    path('productos/',producto, name="producto"),
    path('carrito/',compra, name="carrito"),
    path('formularioCliente/',registroCliente, name= "formularioCliente"),
    path('registroProducto/', registroProducto, name = "registroProducto")
]