from django.shortcuts import render, HttpResponse
from django.http import HttpResponse
from playground_app.models import Curso

# Create your views here.

def curso(request):
      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"
      return HttpResponse(documentoDeTexto)


def inicio(request):
      return render(request, "playground_app/inicio.html")

def cursos(request):
      return render(request, "playground_app/cursos.html")

def profesores(request):
      return render(request, "playground_app/profesores.html")

def estudiantes(request):
      return render(request, "playground_app/estudiantes.html")

def entregables(request):
      return render(request, "playground_app/entregables.html")