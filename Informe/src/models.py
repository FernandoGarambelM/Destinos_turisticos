from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()

    def __str__(self):
        return self.nombre

class NotasAlumnosPorCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.FloatField()

    def __str__(self):
        return f"{self.alumno} - {self.curso} - {self.nota}"
