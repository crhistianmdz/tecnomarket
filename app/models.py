from django.db import models
from django.db.models.base import Model
from django.db.models.fields import CharField

# Create your models here.

class Marca(models.Model):
    nombre=models.CharField(max_length=50)
    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre=models.CharField(max_length=50)
    precio=models.IntegerField()
    descripcion=models.TextField()
    nuevo=models.BooleanField()
    marca=models.ForeignKey(Marca,on_delete=models.PROTECT)
    fecha_fabricacion=models.DateField()
    imagen=models.ImageField(upload_to="productos",null=True)

    def __str__(self):
        return self.nombre

class Contacto(models.Model):
    opciones_consultas=[
        [0,"consulta"],
        [1,'reclamo'],
        [2,'sugerencia'],
        [3,'felicitaciones']
    ]

    nombre=models.CharField(max_length=50)
    corre=models.EmailField()
    tipo_consulta=models.IntegerField(choices=opciones_consultas)
    mensaje=models.TextField()
    avisos=models.BooleanField()

    def __str__(self):
        return self.nombre