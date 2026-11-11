from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

def curso(request):
      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"
      return HttpResponse(documentoDeTexto)

def inicio(request):
      return render(request, "AppCoder/inicio.html")

def estudiantes(request):
      if request.method == 'POST':
            miFormulario = EstudianteFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  estudiante = Estudiante (nombre=informacion['nombre'], apellido=informacion['apellido'],
                   email=informacion['email'])
                  estudiante.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario= EstudianteFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/estudiantes.html", {"miFormulario":miFormulario})

def entregables(request):
      return render(request, "AppCoder/entregables.html")

def cursos(request):
      if request.method == 'POST':
            miFormulario = CursoFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  curso = Curso (nombre=informacion['curso'], camada=informacion['camada'])
                  curso.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario= CursoFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/cursos.html", {"miFormulario":miFormulario})

def profesores(request):
      if request.method == 'POST':
            miFormulario = ProfesorFormulario(request.POST) #aquí mellega toda la información del html
            print(miFormulario)
            if miFormulario.is_valid:   #Si pasó la validación de Django
                  informacion = miFormulario.cleaned_data
                  profesor = Profesor (nombre=informacion['nombre'], apellido=informacion['apellido'],
                  email=informacion['email'], profesion=informacion['profesion'])
                  profesor.save()
                  return render(request, "AppCoder/inicio.html") #Vuelvo al inicio o a donde quieran
      else:
            miFormulario= ProfesorFormulario() #Formulario vacio para construir el html
      return render(request, "AppCoder/profesores.html", {"miFormulario":miFormulario})

def BusquedaCamada(request):
      return render(request, "AppCoder/busquedaCamada.html")

def buscar(request):
      if  request.GET["camada"]:
            camada = request.GET['camada']
            cursos = Curso.objects.filter(camada__iexact=camada)
            return render(request, "AppCoder/inicio.html", {"cursos":cursos, "camada":camada})
      else:
              respuesta = "No enviaste datos"
      return render(request, respuesta)

def leerProfesores(request):
      profesores = Profesor.objects.all() #trae todos los profesores
      contexto= {"profesores":profesores}
      return render(request, "AppCoder/leerProfesores.html",contexto)

def eliminarProfesor(request, profesor_nombre):
      if request.method == 'DELETE':
            try:
                  profesor = Profesor.objects.get(nombre=profesor_nombre)
                  profesor.delete()
            except Profesor.DoesNotExist:
                  pass
      # Redirigimos a la lista de profesores
      profesores = Profesor.objects.all()
      contexto= {"profesores":profesores}
      return render(request, "AppCoder/leerProfesores.html",contexto)

def eliminarEstudiante(request, estudiante_nombre):
      try:
            estudiante = Estudiante.objects.get(nombre=estudiante_nombre)
            estudiante.delete()
      except Estudiante.DoesNotExist:
            # Si no existe, simplemente redirigimos a la lista
            pass
      # Redirigimos a la lista de profesores
      estudiantes = Estudiante.objects.all() #trae todos los estudiantes
      contexto= {"estudiantes":estudiantes}
      return render(request, "AppCoder/leerEstudiantes.html",contexto)

def editarProfesor(request, profesor_nombre):
      # Recibe el nombre del profesor que vamos a modificar
      try:
            profesor = Profesor.objects.get(nombre=profesor_nombre)
      except Profesor.DoesNotExist:
            # si no existe, redirigimos a la lista
            return redirect('LeerProfesores')

      if request.method == 'POST':
            miFormulario = ProfesorFormulario(request.POST)
            if miFormulario.is_valid():
                  informacion = miFormulario.cleaned_data
                  profesor.nombre = informacion['nombre']
                  profesor.apellido = informacion['apellido']
                  profesor.email = informacion['email']
                  profesor.profesion = informacion['profesion']
                  profesor.save()
                  return redirect('LeerProfesores')
            else:
                  # Formulario inválido: mostramos errores
                  return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

      # En caso que no sea POST: creamos el formulario con los datos que vamos a modificar
      miFormulario = ProfesorFormulario(initial={
            'nombre': profesor.nombre,
            'apellido': profesor.apellido,
            'email': profesor.email,
            'profesion': profesor.profesion,
      })

      # Voy al html que me permite editar
      return render(request, "AppCoder/editarProfesor.html", {"miFormulario": miFormulario, "profesor_nombre": profesor_nombre})

class CursoList(ListView):
      model = Curso 
      template_name = "AppCoder/cursos_list.html"

class CursoDetalle(DetailView):
      model = Curso
      template_name = "AppCoder/curso_detalle.html"

class CursoCreacion(CreateView):
      model = Curso
      success_url = "/AppCoder/curso/list"
      fields = ['nombre', 'camada']

class CursoUpdate(UpdateView):
      model = Curso
      success_url = "/AppCoder/curso/list"
      fields  = ['nombre', 'camada']

class CursoDelete(DeleteView):
      model = Curso
      success_url = "/AppCoder/curso/list"

def leerCursos(request):
      cursos = Curso.objects.all() #trae todos los cursos
      contexto= {"cursos":cursos}
      return render(request, "AppCoder/leerCursos.html",contexto)


def leerEstudiantes(request):
      estudiantes =Estudiante.objects.all()  # trae todos los estudiantess
      contexto = {"estudiantes": estudiantes}
      return render(request, "AppCoder/leerEstudiantes.html", contexto)
