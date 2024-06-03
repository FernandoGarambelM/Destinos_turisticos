from django import forms
from .models import Alumno, Curso, NotasAlumnosPorCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class NotasAlumnosPorCursoForm(forms.ModelForm):
    class Meta:
        model = NotasAlumnosPorCurso
        fields = '__all__'
