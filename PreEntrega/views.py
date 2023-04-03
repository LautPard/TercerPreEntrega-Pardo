from django.shortcuts import render
from PreEntrega.models import Tarea, Persona, Materia
from PreEntrega.forms import PersonaForm, BuscarPersonasForm, MateriaForm, BuscarMateriaForm, TareaForm, BuscarTareaForm
from django.views.generic import ListView

def mostrar_mis_tareas(request, criterio):
    if criterio == "todo":
        tareas = Tarea.objects.all()
    else:
        tareas = Tarea.objects.filter(nombre=criterio).all()

    return render(request, "PreEntrega/tareas.html", {"tareas": tareas})


def mostrar_personas(request):
    personas = Persona.objects.all()
    total_personas = len(personas)
    context = {
        "personas": personas,
        "total_personas":total_personas,
        "form": PersonaForm(),
    }
    return render(request, "PreEntrega/personas.html", context)

def cargar_personas(request):
    f = PersonaForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Persona(nombre=f.data["nombre"], apellido=f.data["apellido"], fecha_nacimiento=f.data["fecha_nacimiento"]).save()
        context['form'] = PersonaForm()

    context["personas"] = Persona.objects.all()
    context["total_personas"] = len(Persona.objects.all())
        
    
    return render(request, "PreEntrega/personas.html", context)

def mostrar_materias(request):
    materias = Materia.objects.all()
    context = {
        "materias": materias,
    }
    return render(request, "PreEntrega/materias.html", context)


def cargar_materias(request):
    f = MateriaForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Materia(nombre=f.data["nombre"], año=f.data["año"]).save()
        context['form'] = MateriaForm()

    context["materias"] = Materia.objects.all()
    return render(request, "PreEntrega/materias.html", context)

class BuscarPersonas(ListView):
    model = Persona
    context_object_name = "personas"

    def get_queryset(self):
        f = BuscarPersonasForm(self.request.GET)
        if f.is_valid():
            return Persona.objects.filter(nombre__icontains=f.data["criterio_nombre"]).all()
        return Persona.objects.none()
        

class BuscarMaterias(ListView):
    model = Materia
    context_object_name = "materias"
    
    def get_queryset(self):
        f = BuscarMateriaForm(self.request.GET)

        return Materia.objects.filter(nombre__icontains=f.data["materia"]).all()
    
def agregar_tarea(request):
    f = TareaForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Tarea(tarea=f.data["tarea"], lugar=f.data["lugar"]).save()
        context['form'] = TareaForm()

    context["tareas"] = Tarea.objects.all()
    return render(request, "PreEntrega/tareas.html", context)

class BuscarTareas(ListView):
    model = Tarea
    context_object_name = "tareas"
    
    def get_queryset(self):
        f = BuscarTareaForm(self.request.GET)
        if f.is_valid():
            return Tarea.objects.filter(tarea__icontains=f.data["tarea"]).all()
        return Tarea.objects.none()
        
        
        

