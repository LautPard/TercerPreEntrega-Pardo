from django.db import models

class Tarea(models.Model):
    tarea = models.TextField(max_length=100)
    lugar = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.lugar} - {self.tarea}"
    
class Persona(models.Model):
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.id} - {self.nombre} - {self.apellido}"
    
class Materia(models.Model):
    nombre = models.TextField(max_length=100)
    año = models.TextField(max_length=100)

    def __str__(self):
        return f"{self.año}° - {self.nombre}"
