from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre=models.CharField(max_length=40)
    camada = models.IntegerField()

class Estudiante(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()

class Profesor(models.Model):
    nombre= models.CharField(max_length=30)
    apellido= models.CharField(max_length=30)
    email= models.EmailField()
    profesion= models.CharField(max_length=30)

class Entregable(models.Model):
    nombre= models.CharField(max_length=30)
    fechaDeEntrega = models.DateField()  
    entregado = models.BooleanField()

class Pruebas(models.Model):
    id = models.AutoField
    prioridad = models.CharField(max_length=10)
    descrpcion = models.CharField(max_length=100)
    positividad_negatividad = models.CharField(max_length=1)
    fecha_creacion = models.DateField()
    fecha_actualización = models.DateField()
    pasos_a_reproducir = models.CharField(max_length=10)
    precondicion = models.CharField(max_length=50)
    set_de_datos = models.CharField(max_length=50)
    fecha_ejecucion = models.DateField()
    resultado_esperado = models.CharField(max_length=50)
    resultado_obtenido = models.CharField(max_length=50)
    estado = models.CharField(max_length=20)

