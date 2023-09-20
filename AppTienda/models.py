from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f'Sr(a){self.nombre} {self.direccion} {self.email}'

class Producto(models.Model): 
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=6, decimal_places=2) 

    def __str__(self):
        return f'El {self.nombre} {self.descripcion} {self.precio}'

class Compra(models.Model):
    cliente = models.CharField(max_length=100)
    productos = models.ManyToManyField(Producto, blank=True)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
        return f'El {self.cliente} {self.productos} {self.cantidad}'


class Cupon(models.Model):
    codigo = models.CharField(max_length=50, unique=True)
    descripcion = models.TextField()

    def __str__(self):
        return self.codigo
