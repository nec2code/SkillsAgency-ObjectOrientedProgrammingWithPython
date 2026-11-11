from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso

# Create your views here.

def curso(request):
      curso01 =  Curso(nombre="Desarrollo web", camada="19881")
      curso01.save()
      documentoDeTexto = f"--->Curso: {curso01.nombre}   Camada: {curso01.camada}"
      return HttpResponse(documentoDeTexto)

def inicio(request):
      return render(request, "AppCoder/inicio.html")

def cursos(request):
      return render(request, "AppCoder/cursos.html")

def profesores(request):
      return render(request, "AppCoder/profesores.html")

def estudiantes(request):
      return render(request, "AppCoder/estudiantes.html")

def entregables(request):
      return render(request, "AppCoder/entregables.html")