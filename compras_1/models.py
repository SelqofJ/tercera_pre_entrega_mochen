from django.db import models


class Productos(models.Model):
    nombre = models.CharField(max_length=256)

    def __str__(self):
        return f"{self.nombre}"



class Clientes(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nac = models.DateField()
    
    def __str__(self):
        return f"{self.nombre}, {self.apellido}"

class Estado_producto(models.Model):
    fecha_vencimiento = models.DateTimeField()
    fresco = models.BooleanField(default=False)
    congelado = models.BooleanField(default=False)
    
    def __str__(self):
        return f"{self.fresco}, {self.congelado}"


class Comentarios(models.Model):
    comments = models.TextField()

    def __str__(self):
        return f"{self.comments}"






