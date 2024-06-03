from django.urls import path
from . import views

urlpatterns = [
    path('', views.gestionar_datos, name='gestionar_datos'),
    path('agregar_alumno/', views.agregar_alumno, name='agregar_alumno'),
    path('agregar_curso/', views.agregar_curso, name='agregar_curso'),
    path('agregar_nota/', views.agregar_nota, name='agregar_nota'),
]
