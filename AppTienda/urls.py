from django.urls import path
from .views import *

urlpatterns = [
    path('cliente/',registroCliente, name="cliente"),
    path('productos/',registroProducto, name="producto"),
    path('compra/',crear_cupon, name="compra"),
    
]