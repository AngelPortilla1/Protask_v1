from django.urls import path
from . import views 

urlpatterns = [
    #Dejar la ruta vacia es el estandar para la ruta principal de una aplicacion
    path('', views.lista_proyectos, name='projects'),
    path('create/', views.crear_proyecto, name='create_project')
]