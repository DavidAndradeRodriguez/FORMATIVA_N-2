from django.db import models

# Create your models here.
class Plan(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    precio = models.PositiveIntegerField()
    stock = models.PositiveSmallIntegerField()
    descripcion = models.TextField(blank=True)
    orden = models.PositiveSmallIntegerField(default=1)
    class Meta:
        ordering = ['orden']
 
    def __str__(self):
        return self.nombre
class Reparacion(models.Model):
    nombre = models.CharField(max_length=120)
    precio = models.PositiveIntegerField
    stock = models.PositiveSmallIntegerField()
    descripcion = models.TextField(blank=True)
    categoria = models.ForeignKey(
        Plan,
        on_delete=models.PROTECT,
        related_name='Reparaciones',
    )