from django.shortcuts import render, redirect
from .models import Alumno, Curso, NotasAlumnosPorCurso
from .forms import AlumnoForm, CursoForm, NotasAlumnosPorCursoForm

def gestionar_datos(request):
    alumnos = Alumno.objects.all()
    cursos = Curso.objects.all()
    notas = NotasAlumnosPorCurso.objects.all()

    context = {
        'alumno_form': AlumnoForm(prefix='alumno'),
        'curso_form': CursoForm(prefix='curso'),
        'nota_form': NotasAlumnosPorCursoForm(prefix='nota'),
        'alumnos': alumnos,
        'cursos': cursos,
        'notas': notas
    }

    return render(request, 'gestion_alumnos/gestionar_datos.html', context)
def agregar_alumno(request):
    if request.method == "POST":
        alumno_form = AlumnoForm(request.POST, prefix='alumno')
        if alumno_form.is_valid():
            alumno_form.save()
        return redirect('gestionar_datos')

def agregar_curso(request):
    if request.method == "POST":
        curso_form = CursoForm(request.POST, prefix='curso')
        if curso_form.is_valid():
            curso_form.save()
        return redirect('gestionar_datos')

def agregar_nota(request):
    if request.method == "POST":
        nota_form = NotasAlumnosPorCursoForm(request.POST, prefix='nota')
        if nota_form.is_valid():
            nota_form.save()
        return redirect('gestionar_datos')