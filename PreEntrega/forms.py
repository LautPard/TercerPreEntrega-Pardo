from django import forms

class PersonaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()

class BuscarPersonasForm(forms.Form):
    criterio_nombre = forms.CharField(max_length=100)
    
class MateriaForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    año = forms.CharField(max_length=100)

class BuscarMateriaForm(forms.Form):
    materias = forms.CharField(max_length=100)

class TareaForm(forms.Form):
    tarea = forms.CharField(max_length=100)
    lugar = forms.CharField(max_length=100)

class BuscarTareaForm(forms.Form):
    tarea = forms.CharField(max_length=100)


