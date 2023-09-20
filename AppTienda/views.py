from django.shortcuts import render
from .models import *
from . forms import ClienteForm, CompraCarrito, Productos, CuponForm




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

def registroCompra(req):
      if req.method == 'POST':
        form= CompraCarrito(req.POST)
        if form.is_valid():
            form.save()
      else:
          form = CompraCarrito()
      return render(req, 'compra.html', {'form': form})

def crear_cupon(req):
    if req.method == 'POST':
        form = CuponForm(req.POST)
        if form.is_valid():
            form.save()
         
    else:
        form = CuponForm()
    
    return render(req, 'compra.html', {'form': form})