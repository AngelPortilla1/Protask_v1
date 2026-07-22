from django.contrib import admin
from django.urls import path, include
from projects.views import lista_proyectos, crear_proyecto

 #"Cualquier ruta que comience con projects/, va a buscar al archivo urls.py de la aplicación projects
urlpatterns = [
    path('admin/', admin.site.urls),
    path('projects/', include('projects.urls')),
]