from django.shortcuts import render
from .models import *
from . forms import ClienteForm, Productos
# Create your views here.


def inicio(req):
   return render(req, "inicio.html")

def cliente(req):
    return render(req, "cliente.html")

def producto(req): 
    return render(req, "productos.html")

def compra(req): 
    return render(req, "compra.html")

def registroCliente(req):
    if req.method == 'POST':
        form = ClienteForm(req.POST)
        if form.is_valid():
            form.save()

    else:
        form = ClienteForm()
    return render(req, 'cliente.html', {'form': form})

def registroProducto(req):    
       if req.method == 'POST':
        form = Productos(req.POST)
        if form.is_valid():
            form.save()

       else:
        form = Productos()
       return render(req, 'productos.html', {'form': form})
