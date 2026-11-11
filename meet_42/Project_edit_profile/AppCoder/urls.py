from django.urls import path
from AppCoder import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.inicio, name="Inicio"), #esta era nuestra primer view
    path('cursos', views.cursos, name="Cursos"),
    path('profesores', views.profesores, name="Profesores"),
    path('estudiantes', views.estudiantes, name="Estudiantes"),
    path('entregables', views.entregables, name="Entregables"),
    path('cursoFormulario', views.cursos, name="CursoFormulario"),
    path('profesorFormulario', views.profesores, name="ProfesorFormulario"),
    path('estudianteFormulario', views.estudiantes, name="EstudianteFormulario"),
    path('busquedaCamada',  views.BusquedaCamada, name="BusquedaCamada"),
    path('leerProfesores', views.leerProfesores, name="LeerProfesores"),
    path('leerCursos', views.leerCursos, name="leerCursos"),
    path('leerEstudiantes', views.leerEstudiantes, name="leerEstudiantes"),
    path('eliminarProfesor/<str:profesor_nombre>/', views.eliminarProfesor, name="eliminarProfesor"),
    path('editarProfesor/<str:profesor_nombre>/', views.editarProfesor, name="editarProfesor"),
    path('eliminarEstudiante/<str:estudiante_nombre>/', views.eliminarEstudiante, name="eliminarEstudiante"),
    path('buscar/', views.buscar),
    path('login', views.login_request, name = 'Login'),
    path('register', views.register, name = 'Register'),
    path('logout', views.logout_request, name = 'Logout'),
    path('editarPerfil', views.editarPerfil, name = 'editarPerfil'),
]   
