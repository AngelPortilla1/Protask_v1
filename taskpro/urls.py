from django.contrib import admin
from django.urls import path
from projects.views import lista_proyectos, crear_proyecto


urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', lista_proyectos, name='projects'),
    path('projects/create/', crear_proyecto, name='create_project')
]