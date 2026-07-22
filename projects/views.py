
from django.shortcuts import render


def lista_proyectos(request):
    # render toma 3 parámetros: el request, la ruta del html, y (opcionalmente) datos.
    return render(request, 'projects/lista.html')


def crear_proyecto(request):
    return render(request, 'projects/crear.html')