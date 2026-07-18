from django.http import HttpResponse 


def lista_proyectos(request):
    return HttpResponse("Lista de proyectos")


def crear_proyecto(request):
    return HttpResponse("Crear proyecto")