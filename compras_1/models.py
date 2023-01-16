from django.db import models


class Productos(models.Model):
    nombre = models.CharField(max_length=256)



class Clientes(models.Model):
    nombre = models.CharField(max_length=256)
    apellido = models.CharField(max_length=256)
    dni = models.CharField(max_length=32)
    email = models.EmailField()
    fecha_nac = models.DateField()

class Estado_producto(models.Model):
    fecha_vencimiento = models.DateTimeField()
    fresco = models.BooleanField(default=False)
    congelado = models.BooleanField(default=False)


class Comentarios(models.Model):
    comments = models.TextField()






