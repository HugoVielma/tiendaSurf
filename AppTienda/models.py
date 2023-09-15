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
    cliente = models.ForeignKey(Cliente, on_delete= models.CASCADE)
    productos = models.ManyToManyField(Producto)
    cantidad = models.IntegerField(default=0)

    def __str__(self):
      return f'Su compra, Sr(a) {self.cliente.nombre}, es de: {", ".join([producto.nombre for producto in self.productos.all()])} con una cantidad de: {self.cantidad}'
