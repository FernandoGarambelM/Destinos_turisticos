from django.shortcuts import render, redirect
from .models import Destination
from .forms import DestinosTuristicosForm
# Create your views here.

def index(request):
   
    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})

def añadir_destino(request):
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DestinosTuristicosForm()
    return render(request, 'administrador.html', {'form': form})

def modificar_destino(request, id):
    destino = Destination.objects.get(id=id)
    if request.method == 'POST':
        form = DestinosTuristicosForm(request.POST, request.FILES, instance=destino)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = DestinosTuristicosForm(instance=destino)
    return render(request, 'administrador.html', {'form': form, 'destino': destino})

def eliminar_destino(request, id):
    destino = Destination.objects.get(id=id)
    if request.method == 'POST':
        destino.delete()
        return redirect('index')
    return render(request, 'administrador.html', {'destino': destino})