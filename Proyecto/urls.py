"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from PreEntrega.views import (
                            mostrar_mis_tareas,
                            mostrar_personas, 
                            cargar_personas, 
                            BuscarPersonas,
                            mostrar_materias,
                            cargar_materias,
                            BuscarMaterias,
                            agregar_tarea,
                            BuscarTareas)
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mis-tareas', mostrar_mis_tareas, name="mis-tareas"),
    path('mis-tareas/agregar',agregar_tarea,name="tareas-agregar"),
    path('mis-tareas/list',BuscarTareas.as_view(),name="tareas-list"),
    path('personas', mostrar_personas, name="personas"),
    path('personas/create', cargar_personas,name="personas-create"),
    path('personas/list', BuscarPersonas.as_view(), name="personas-list"),
    path('materias/cargar', cargar_materias, name="materias-cargar"),
    path('materias/list', BuscarMaterias.as_view(),name="materias-list"),
    path('materias',mostrar_materias,name="materias"),
]
