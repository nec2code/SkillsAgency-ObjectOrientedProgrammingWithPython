from typing import List
from django.http.request import QueryDict
from django.shortcuts import redirect, render, HttpResponse
from django.http import HttpResponse
from AppCoder.models import Curso, Profesor, Estudiante
from AppCoder.forms import CursoFormulario, ProfesorFormulario, EstudianteFormulario, UserEditForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

def curso(request):
      curso =  Curso(nombre="Desarrollo web", camada="19881")
      curso.save()
      documentoDeTexto = f"--->Curso: {curso.nombre}   Camada: {curso.camada}"
      return HttpResponse(documentoDeTexto)

@login_required
def inicio(request):
      return render(request, "AppCoder/inicio.html")

@login_required
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
            cursos = Curso.objects.filter(camada__icontains=camada)
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

def login_request(request):
      if request.method == "POST":
            form = AuthenticationForm(request, data=request.POST)
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contrasena = form.cleaned_data.get('password')
                  user = authenticate(username=usuario, password=contrasena)

                  if user is not None:
                        login(request, user)
                        return render(request, "AppCoder/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
                  else:
                        # Usuario o contraseña incorrectos
                        form.add_error(None, "Usuario o contraseña incorrectos")
                        return render(request, "AppCoder/login.html", {"form": form})
            else:
                  # El formulario tiene errores de validación
                  return render(request, "AppCoder/login.html", {"form": form})
      form = AuthenticationForm()
      return render(request, "AppCoder/login.html", {"form": form})

def register(request):
      if request.method == "POST":
            form = UserCreationForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request, "AppCoder/registro.html", {"mensaje": f"Usuario {username} creado exitosamente"})
            else:
                  # Si el formulario no es válido, volvemos a mostrar el formulario con los errores
                  return render(request, "AppCoder/registro.html", {"form": form})
      else:
            form = UserCreationForm()
            return render(request, "AppCoder/registro.html", {"form": form})

def logout_request(request):
      """Cierra la sesión del usuario y muestra una pantalla de confirmación."""
      logout(request)
      return render(request, "AppCoder/logout.html")

@login_required
def editarPerfil(request):
      usuario = request.user
      if request.method == "POST":
            miFormulario = UserEditForm(request.POST, instance=usuario)
            if miFormulario.is_valid():
                  miFormulario.save()
                  return render(request, "AppCoder/inicio.html", {"mensaje": "Perfil actualizado exitosamente!"})
      else:
            miFormulario = UserEditForm(instance=usuario, initial={"email": usuario.email})

      return render(request, "AppCoder/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})